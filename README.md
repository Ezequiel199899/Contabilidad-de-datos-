cash-flow-predictor.    app.py
requirements.txt
README.mdv.    flask
flask_sqlalchemy.       from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))  # income / expense
    amount = db.Column(db.Float)
    currency = db.Column(db.String(3))  # ARS / USD
    date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def home():
    return jsonify({"message": "Cash Flow API Running"})

@app.route("/add", methods=["POST"])
def add_transaction():
    data = request.json
    
    transaction = Transaction(
        type=data["type"],
        amount=data["amount"],
        currency=data["currency"]
    )
    
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({"message": "Transaction added"}), 201

@app.route("/balance", methods=["GET"])
def get_balance():
    transactions = Transaction.query.all()
    balance = {"ARS": 0, "USD": 0}

    for t in transactions:
        if t.type == "income":
            balance[t.currency] += t.amount
        else:
            balance[t.currency] -= t.amount

    return jsonify(balance)

@app.route("/forecast", methods=["GET"])
def forecast():
    transactions = Transaction.query.all()
    
    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expense = sum(t.amount for t in transactions if t.type == "expense")

    projection = total_income - total_expense

    return jsonify({
        "projected_balance_next_30_days": projection
    })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True).       # Cash Flow Predictor

Simple cash flow management API with ARS/USD support.
Focused on small businesses liquidity control.

## Features
- Income & expense tracking
- Multi-currency (ARS/USD)
- Balance calculation
- 30-day projection

## Tech Stack
- Python
- Flask
- SQLite

## Run locally

pip install -r requirements.txt
python app.py.       git init
git add .
git commit -m "Initial MVP - Cash Flow Predictor"
git branch -M main
git remote add origin https://github.com/Ezequiel199899/cash-flow-predictor.git
git push -u origin main.     cash-flow-predictor/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── login.html
│   ├── register.html
│   └── dashboard.html.     flask
flask_sqlalchemy
flask_login
werkzeug. from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ------------------ MODELS ------------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))
    amount = db.Column(db.Float)
    currency = db.Column(db.String(3))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard"))
    
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        transaction = Transaction(
            type=request.form["type"],
            amount=float(request.form["amount"]),
            currency=request.form["currency"],
            user_id=current_user.id
        )
        db.session.add(transaction)
        db.session.commit()

    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    
    balance = {"ARS": 0, "USD": 0}
    for t in transactions:
        if t.type == "income":
            balance[t.currency] += t.amount
        else:
            balance[t.currency] -= t.amount

    return render_template("dashboard.html", balance=balance, transactions=transactions)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.crea.    <h2>Register</h2>
<form method="POST">
    <input type="text" name="username" placeholder="Username" required><br>
    <input type="password" name="password" placeholder="Password" required><br>
    <button type="submit">Register</button>
</form>
<a href="/login">Login</a>.     te_all()
    app.run(debug=True).    <h2>Dashboard</h2>

<h3>Add Transaction</h3>
<form method="POST">
    <select name="type">
        <option value="income">Income</option>
        <option value="expense">Expense</option>
    </select><br>

    <input type="number" step="0.01" name="amount" placeholder="Amount" required><br>

    <select name="currency">
        <option value="ARS">ARS</option>
        <option value="USD">USD</option>
    </select><br>

    <button type="submit">Add</button>
</form>

<h3>Balance</h3>
<p>ARS: {{ balance["ARS"] }}</p>
<p>USD: {{ balance["USD"] }}</p>

<h3>Transactions</h3>
<ul>
{% for t in transactions %}
    <li>{{ t.type }} - {{ t.amount }} {{ t.currency }}</li>
{% endfor %}
</ul>

<a href="/logout">Logout</a>.      pip install -r requirements.txt
python app.py.  pip install -r requirements.txt
python app.py.  http://127.0.0.1:5000.     requests.  import requests.  def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()
    
    if "result" in data:
        return data["result"]
    return None
     @app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":
        transaction = Transaction(
            type=request.form["type"],
            amount=float(request.form["amount"]),
            currency=request.form["currency"],
            user_id=current_user.id
        )
        db.session.add(transaction)
        db.session.commit()

    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    
    balance = {
        "ARS": 0,
        "USD": 0,
        "EUR": 0,
        "GBP": 0,
        "BRL": 0,
        "CLP": 0,
        "UYU": 0
    }

    for t in transactions:
        if t.type == "income":
            balance[t.currency] += t.amount
        else:
            balance[t.currency] -= t.amount

    # Convertir todo a EUR
    total_in_eur = 0
    for currency, amount in balance.items():
        if amount != 0:
            converted = convert_currency(currency, "EUR", amount)
            if converted:
                total_in_eur += converted

    return render_template(
        "dashboard.html",
        balance=balance,
        total_eur=round(total_in_eur, 2),
        transactions=transactions
    ).   <select name="currency">
    <option value="ARS">ARS</option>
    <option value="USD">USD</option>
    <option value="EUR">EUR</option>
    <option value="GBP">GBP</option>
    <option value="BRL">BRL</option>
    <option value="CLP">CLP</option>
    <option value="UYU">UYU</option>
</select>.  <h3>Total convertido a EUR</h3>
<p>{{ total_eur }} EUR</p>.            contabilidad-de-datos
│
├── main.py
├── requirements.txt
│
├── automation
│   ├── alerts.py
│   └── predictions.py
│
├── analysis
│   └── pipeline.py
│
├── data
│
└── README.md.      import pandas as pd

def detect_anomalies(df):
    alerts = []
    
    avg_expense = df["expenses"].mean()

    for value in df["expenses"]:
        if value > avg_expense * 1.5:
            alerts.append("High expense anomaly detected").      from sklearn.linear_model import LinearRegression
import numpy as np

def predict_trend(data):
    
    X = np.array(range(len(data))).reshape(-1,1)
    y = np.array(data)

    model = LinearRegression()
    model.fit(X,y)

    next_value = model.predict([[len(data)]])
    
    return next_value[0]

    return alerts.      from automation.alerts import detect_anomalies
from automation.predictions import predict_trend

def run_analysis(df):

    alerts = detect_anomalies(df)

    prediction = predict_trend(df["income"]).       import pandas as pd
from analysis.pipeline import run_analysis

def main():

    df = pd.read_csv("data/financial_data.csv")

    results = run_analysis(df)

    print("Analysis Results")
    print("----------------")

    print("Alerts:")
    for alert in results["alerts"]:
        print("-", alert)

    print("\nNext income prediction:", results["next_income_prediction"])


if __name__ == "__main__":
    main().            pandas
numpy
scikit-learn.    # Automated Financial Data Analysis Platform

## Overview

This project is an automated financial data analysis platform built with Python.

The system analyzes financial datasets, detects anomalies in expenses, and predicts future financial trends using machine learning techniques.

## Features

- Automated financial data analysis
- Expense anomaly detection
- Income trend prediction
- Modular automation architecture

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn

## Architecture

Data → Processing → Analysis → Prediction

## Demo

Vercel App:
https://TU-LINK-DE-VERCEL

## Repository

GitHub:
https://github.com/Ezequiel199899/Contabilidad-de-datos-

## Project Status

Active Development

## Roadmap

- AI-generated financial insights

    return {
        "alerts": alerts,
        "next_income_prediction": prediction
    }