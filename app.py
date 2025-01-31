import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Database connection details
db_config = {
    'host': 'localhost',
    'user': 'root', 
    'password': '1234',  
    'database': 'personel_expenses'  
}

# Function to connect to the database
def get_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        st.error(f"Database Connection Error: {err}")
        return None

# Function to fetch expenses data
def fetch_expenses_data():
    connection = get_connection()
    if connection:
        query = "SELECT * FROM expenses_all"
        data = pd.read_sql_query(query, connection)
        connection.close()
        return data
    return pd.DataFrame()

# Streamlit UI setup
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")
st.title("📊 Personal Expense Analyzer")
st.markdown("**Gain insights into your spending habits with detailed analytics.**")

# Fetch data
expenses_data = fetch_expenses_data()

if not expenses_data.empty:
    # Convert date column to datetime format
    expenses_data['date'] = pd.to_datetime(expenses_data['date'])
    expenses_data['month'] = expenses_data['date'].dt.strftime('%Y-%m')
    
    # Sidebar Filters
    st.sidebar.header("🔍 Filter Data")
    months = expenses_data['month'].unique()
    selected_month = st.sidebar.selectbox("Select Month", months)
    categories = expenses_data['category'].unique()
    selected_category = st.sidebar.multiselect("Select Category", categories, default=categories)
    
    # Filter data based on selections
    filtered_data = expenses_data[(expenses_data['month'] == selected_month) & (expenses_data['category'].isin(selected_category))]
    
    # KPIs
    total_expense = filtered_data['amount_paid'].sum()
    total_cashback = filtered_data['cashback'].sum()
    avg_expense = filtered_data['amount_paid'].mean()
    
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    kpi_col1.metric("💸 Total Expense", f"${total_expense:,.2f}")
    kpi_col2.metric("🎁 Total Cashback", f"${total_cashback:,.2f}")
    kpi_col3.metric("📊 Avg Expense per Transaction", f"${avg_expense:,.2f}")
    
    # Expense Breakdown (Bar Chart)
    st.subheader("📊 Expense Breakdown by Category")
    category_data = filtered_data.groupby('category')['amount_paid'].sum().reset_index()
    fig_bar = px.bar(category_data, x='category', y='amount_paid', color='category', text_auto='.2s')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Expense Distribution (Pie Chart)
    st.subheader("🎯 Expense Distribution")
    fig_pie = px.pie(category_data, names='category', values='amount_paid', hole=0.3)
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Monthly Trend (Line Chart)
    st.subheader("📈 Monthly Expense Trend")
    trend_data = expenses_data.groupby('month')['amount_paid'].sum().reset_index()
    fig_line = px.line(trend_data, x='month', y='amount_paid', markers=True, title='Total Monthly Expenses')
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Cashback vs. Expenses (Scatter Plot)
    st.subheader("💰 Cashback vs. Expenses")
    fig_scatter = px.scatter(filtered_data, x='amount_paid', y='cashback', color='category', size='cashback', hover_data=['description'])
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Display raw data
    st.subheader("🗃️ Detailed Transactions")
    st.dataframe(filtered_data)
else:
    st.error("No expense data available. Please check your database connection.")
