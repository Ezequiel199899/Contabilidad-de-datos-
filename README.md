cashflow-ai/
│
├── app/
│   └── app.py
│
├── data/
│   └── sample_data.csv
│
├── models/
│   └── model.py
│
├── utils/
│   └── preprocessing.py
│
├── requirements.txt
└── README.md       import streamlit as st
import pandas as pd
from models.model import detectar_anomalias, predecir

st.title("Cash Flow AI Platform")

uploaded_file = st.file_uploader("Subí tu CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Datos")
    st.write(df.head())

    st.subheader("Detección de anomalías")
    df["anomalia"] = detectar_anomalias(df)
    st.write(df)

    st.subheader("Predicción")
    pred = predecir(df)
    st.write(pred).     t.             def limpiar_datos(df):
    df = df.dropna()
    return df.   streamlit
pandas
numpy
scikit-learn.     mes,ingresos,gastos
1,1000,800
2,1200,900
3,900,850
4,1500,1000
5,1300,950.       # Cash Flow AI Platform

Aplicación de análisis financiero con inteligencia artificial.

## Funcionalidades
- Predicción de flujo de caja
- Detección de anomalías
- Visualización de datos

## Tecnologías
- Python
- Pandas
- Scikit-learn
- Streamlit

## Cómo ejecutar

```bash
pip install -r requirements.txt
streamlit run app/app.py     