mkdir contabilidad-ai
cd contabilidad-ai.   python -m venv venv
venv\Scripts\activate   # Windows.          pip install fastapi uvicorn pandas scikit-learn numpy.    contabilidad-ai/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│
├── models/
│   └── model.py
│
├── services/
│   ├── prediction.py
│   └── anomalies.py
│
├── utils/
│   └── preprocessing.py
│
├── data/
│   └── sample.csv
│
├── requirements.txt
└── README.md.    from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Contabilidad AI API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}.    from fastapi import APIRouter
from services.prediction import predict_income
from services.anomalies import detect_anomalies

router = APIRouter()

@router.post("/predict")
def predict(data: list):
    return {"prediction": predict_income(data)}

@router.post("/anomalies")
def anomalies(data: list):
    return {"anomalies": detect_anomalies(data)}.           from pydantic import BaseModel
from typing import List

class Transaction(BaseModel):
    amount: float

class Transactions(BaseModel):
    data: List[Transaction].    import pandas as pd

def preprocess(data):
    df = pd.DataFrame(data)
    df["amount"] = df["amount"].astype(float)
    return df.         from sklearn.linear_model import LinearRegression
import numpy as np

model = LinearRegression()

def predict_next(data):
    X = np.arange(len(data)).reshape(-1, 1)
    model.fit(X, data)
    next_index = [[len(data)]]
    prediction = model.predict(next_index)[0]
    return prediction.          from utils.preprocessing import preprocess
from models.model import predict_next

def predict_income(data):
    df = preprocess(data)
    values = df["amount"].values
    return float(predict_next(values)).          import numpy as np

def detect_anomalies(data):
    values = np.array([x["amount"] for x in data])
    mean = np.mean(values)
    std = np.std(values)

    anomalies = []

    for i, v in enumerate(values):
        if abs(v - mean) > 2 * std:
            anomalies.append({"index": i, "value": float(v)})

    return anomalies.         amount
100
200
150
300
500
1200.            uvicorn app.main:app --reload.            [
  {"amount": 100},
  {"amount": 200},
  {"amount": 300}
].            git init
git add .
git commit -m "Proyecto contabilidad AI"
git branch -M main
git remote add origin TU_REPO
git push -u origin main.                     