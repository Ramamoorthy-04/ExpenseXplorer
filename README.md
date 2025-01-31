💰 Personal Expense Analyzer – Track Like a Pro! 📊🔥  

Welcome to Personal Expense Analyzer, your AI-powered (okay, maybe just Faker-powered 🤖) expense-tracking sidekick! Tired of wondering "where all your money goes"? Let’s analyze those expenses with style!  

🎯 What Does This Do?  
This project does three amazing things:  
✅ Generates fake expenses (because why not?) 💸  
✅ Stores & organizes them in a MySQL database 📂  
✅ Visualizes spending habits with interactive graphs 📊  

🚀 Features That'll Make You Rich (Maybe 🤷‍♂️)  
💵 Auto-generated expense data (12 months, 100 entries/month)  
📅 Organized tables for each month + a combined table  
🛠️ MySQL-powered database for secure storage  
📈 Cool visualizations (Bar, Line, Pie, and Area charts)  
⚡ Streamlit UI – Simple, interactive, and fancy!  

🛠️ How to Set It Up? (Super Easy, I Promise)  

1️⃣ Install Dependencies  
First, grab your favorite terminal (or VS Code) and run:  
```sh
pip install mysql-connector-python faker pandas streamlit
```

2️⃣ Set Up the Database  
Fire up MySQL and run:  
```sh
mysql -u root -p
```
Then, run:  
```sh
CREATE DATABASE personel_expenses;
```

3️⃣ Generate Fake Data  
Run the script to populate the database:  
```sh
python generate_expenses.py
```

4️⃣ Launch the Streamlit App 🚀  
```sh
streamlit run app.py
```
Boom! Open your browser, analyze your *fake* (or real) expenses, and act rich 💰😂.  

📊 Visuals You'll Love  
✔ Total expenses per category 📊  
✔ Expense distribution (Pie chart) 🥧  
✔ Monthly spending trends 📉  
✔ Cumulative spending curve 📈  

🔥 Future Enhancements (If You’re Feeling Extra)  
🚀 Add user authentication (so everyone gets their own expenses)  
🎨 Use Plotly for fancier charts  
☁ Deploy it on Streamlit Cloud or AWS
📊 Integrate AI-powered insights (or just make it sound smart 😂)  

🤝 Contributing  
Want to improve it? Fork it, PR it, or just DM me some money 💸.  

🏆 Special Thanks  
MySQL – for keeping our *fake* finances secure  
Streamlit – for making visualizations cool  
Faker – for pretending we have money  

💡Pro Tip: If your expenses are too high, just pretend they're fake! 😉  

🚀Let’s track some money! 🔥💰
