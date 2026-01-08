/
├── api/
│   └── index.py        ← entrypoint Vercel
├── app/
│   ├── main.py         ← FastAPI app
│   ├── models/
│   │   ├── finance.py  ← modelos financieros clásicos
│   │   └── quantum.py  ← modelo cuántico conceptual
│   ├── schemas.py
│   └── services/
│       ├── predictor.py
│       └── quantum_engine.py
├── requirements.txt
└── vercel.json.          fastapi
uvicorn
numpy
pandas
scikit-learn
pydantic.     {
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}.             from app.main import app

# Vercel detecta automáticamente "app".       from fastapi import FastAPI
from app.schemas import FinanceInput
from app.services.predictor import classic_prediction
from app.services.quantum_engine import quantum_prediction

app = FastAPI(
    title="Quantum Finance AI",
    description="Predicciones financieras clásicas + cuánticas",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "model": "Finance AI",
        "modes": ["classic", "quantum-inspired"]
    }

@app.post("/predict/classic")
def predict_classic(data: FinanceInput):
    return classic_prediction(data)

@app.post("/predict/quantum")
def predict_quantum(data: FinanceInput):
    return quantum_prediction(data).          from pydantic import BaseModel

class FinanceInput(BaseModel):
    price_increase: float
    customer_tenure: int
    monthly_spend: float
    competitors: int.              import numpy as np

def classic_prediction(data):
    # Modelo simple simulando churn / riesgo
    score = (
        data.price_increase * 0.4 +
        (1 / (data.customer_tenure + 1)) * 0.3 +
        data.monthly_spend * 0.2 +
        data.competitors * 0.1
    )

    probability = min(score / 100, 1)

    return {
        "type": "classic",
        "churn_probability": round(probability, 3),
        "risk_level": "high" if probability > 0.6 else "medium" if probability > 0.3 else "low"
    }.         import numpy as np

def quantum_prediction(data):
    """
    Modelo cuántico conceptual:
    - superposición de estados
    - colapso probabilístico
    """

    # Estados base (|0>, |1>)
    states = np.array([
        data.price_increase,
        data.monthly_spend,
        data.competitors,
        1 / (data.customer_tenure + 1)
    ])

    # Normalización (amplitudes)
    norm = np.linalg.norm(states)
    amplitudes = states / norm

    # Probabilidad cuántica (|ψ|²)
    probabilities = amplitudes ** 2
    quantum_score = probabilities.sum()

    # Ruido cuántico simulado
    noise = np.random.normal(0, 0.05)
    final_probability = min(max(quantum_score + noise, 0), 1)

    return {
        "type": "quantum-inspired",
        "superposition_state": amplitudes.tolist(),
        "quantum_probability": round(final_probability, 3),
        "interpretation": (
            "Alta inestabilidad del sistema"
            if final_probability > 0.6
            else "Sistema en equilibrio probabilístico"
        )
    }.             import numpy as np

def quantum_prediction(data):
    """
    Modelo cuántico conceptual:
    - superposición de estados
    - colapso probabilístico
    """

    # Estados base (|0>, |1>)
    states = np.array([
        data.price_increase,
        data.monthly_spend,
        data.competitors,
        1 / (data.customer_tenure + 1)
    ])

    # Normalización (amplitudes)
    norm = np.linalg.norm(states)
    amplitudes = states / norm

    # Probabilidad cuántica (|ψ|²)
    probabilities = amplitudes ** 2
    quantum_score = probabilities.sum()

    # Ruido cuántico simulado
    noise = np.random.normal(0, 0.05)
    final_probability = min(max(quantum_score + noise, 0), 1)

    return {
        "type": "quantum-inspired",
        "superposition_state": amplitudes.tolist(),
        "quantum_probability": round(final_probability, 3),
        "interpretation": (
            "Alta inestabilidad del sistema"
            if final_probability > 0.6
            else "Sistema en equilibrio probabilístico"
        )
    }          git add .
git commit -m "Finance AI with quantum-inspired predictions"
git push