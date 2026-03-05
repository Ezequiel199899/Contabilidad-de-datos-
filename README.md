   cash-flow-ai-platform/
│
├── app.py
├── requirements.txt
├── README.md
│
├── analysis
│   ├── alerts.py
│   ├── predictions.py
│   └── pipeline.py
│
├── data
│   └── sample_financial_data.csv
│
└── templates
    ├── login.html
    ├── register.html
    └── dashboard.html.        from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd

from analysis.pipeline import run_analysis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10))
    amount = db.Column(db.Float)
    currency = db.Column(db.String(3))
    date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/")
def home():
    return jsonify({"message": "Cash Flow AI Platform Running"})

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


@app.route("/balance")
def balance():

    transactions = Transaction.query.all()

    balance = {"ARS":0,"USD":0}

    for t in transactions:
        if t.type == "income":
            balance[t.currency] += t.amount
        else:
            balance[t.currency] -= t.amount

    return jsonify(balance)


@app.route("/analysis")
def analysis():

    transactions = Transaction.query.all()

    data = []

    for t in transactions:
        data.append({
            "income": t.amount if t.type == "income" else 0,
            "expenses": t.amount if t.type == "expense" else 0
        })

    df = pd.DataFrame(data)

    results = run_analysis(df)

    return jsonify(results)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True).     import pandas as pd

def detect_anomalies(df):

    alerts = []

    avg_expense = df["expenses"].mean()

    for value in df["expenses"]:

        if value > avg_expense * 1.5:

            alerts.append("High expense anomaly detected")

    return alerts.      from sklearn.linear_model import LinearRegression
import numpy as np

def predict_trend(data):

    X = np.array(range(len(data))).reshape(-1,1)
    y = np.array(data)

    model = LinearRegression()
    model.fit(X,y)

    next_value = model.predict([[len(data)]])

    return float(next_value[0]).    from analysis.alerts import detect_anomalies
from analysis.predictions import predict_trend

def run_analysis(df):

    alerts = detect_anomalies(df)

    prediction = predict_trend(df["income"])

    return {

        "alerts": alerts,
        "next_income_prediction": prediction

    }.      flask
flask_sqlalchemy
pandas
numpy
scikit-learn.     # Cash Flow AI Platform

Automated financial analysis platform built with Python and Flask.

The system tracks financial transactions, calculates balances, detects anomalies in expenses and predicts financial trends using machine learning.

## Features

- Financial transaction tracking
- Multi currency balance calculation
- Automated anomaly detection
- Income trend prediction
- REST API architecture

## Tech Stack

Python  
Flask  
SQLite  
Pandas  
Scikit-learn  

## API Endpoints

GET /
Platform status

POST /add
Add new transaction

GET /balance
Current balance

GET /analysis
Automated financial analysis

## Example Use Case

Small businesses can monitor liquidity, detect abnormal expenses and forecast future income trends.

## Project Status

Active Development

## Future Improvements

- AI generated financial insights
- real-time analytics
- cloud deployment## Example API Request

POST /add

{
 "type": "income",
 "amount": 500,
 "currency": "USD"
}.        @app.route("/health")
def health():
    return {"status": "ok"}.   ## Example Response

GET /analysis

{
 "alerts": ["High expense anomaly detected"],
 "next_income_prediction": 520.34
}