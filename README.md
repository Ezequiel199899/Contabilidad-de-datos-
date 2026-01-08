/
├── main.py
├── quantum_simulator.py
├── requirements.txt
└── vercel.json.            import random
from typing import Dict

def superposed_prediction(input_text: str) -> Dict[str, float]:
    """
    Genera un estado cuántico simulado (superposición).
    """
    estados = {
        "positivo": random.random(),
        "neutral": random.random(),
        "negativo": random.random()
    }

    # Normalización (la suma debe ser 1)
    total = sum(estados.values())
    return {k: v / total for k, v in estados.items()}

def collapse_wavefunction(state_probs: Dict[str, float]) -> str:
    """
    Colapso cuántico: elige un estado según su probabilidad.
    """
    opciones = list(state_probs.keys())
    probabilidades = list(state_probs.values())
    return random.choices(opciones, probabilidades)[0].      from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from quantum_simulator import (
    superposed_prediction,
    collapse_wavefunction
)

app = FastAPI(title="Quantum AI Simulator")

class QuantumRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "Quantum AI running ⚛️"}

@app.post("/quantum_predict")
def quantum_predict(request: QuantumRequest):
    """
    IA cuántica simulada:
    - Superposición
    - Colapso
    """
    state_vector: Dict[str, float] = superposed_prediction(request.text)
    result = collapse_wavefunction(state_vector)

    return {
        "input": request.text,
        "state_vector": state_vector,
        "collapsed_result": result
    }.      fastapi
uvicorn
pydantic.        uvicorn main:app --reload.       {
  "input": "Este proyecto tiene mucho potencial",
  "state_vector": {
    "positivo": 0.48,
    "neutral": 0.31,
    "negativo": 0.21
  },
  "collapsed_result": "positivo"
}.                   