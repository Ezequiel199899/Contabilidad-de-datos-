ai/
├── app/
│   └── app.py
├── models/
│   └── model.py
├── utils/
│   └── preprocessing.py
├── data/
│   └── sample_data.csv
├── requirements.txt
└── README.md.        import streamlit as st
import pandas as pd
from models.model import detectar_anomalias, predecir
from utils.preprocessing import limpiar_datos

st.set_page_config(page_title="Cash Flow AI", layout="wide")

st.title("💸 Cash Flow AI Platform")

uploaded_file = st.file_uploader("Subí tu archivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Datos originales")
    st.write(df.head())

    # Limpieza
    df = limpiar_datos(df)

    st.subheader("🧹 Datos limpios")
    st.write(df.head())

    # Anomalías
    st.subheader("⚠️ Detección de anomalías")
    df["anomalia"] = detectar_anomalias(df)
    st.write(df)

    # Gráfico
    st.subheader("📈 Visualización")
    st.line_chart(df[["ingresos", "gastos"]])

    # Predicción
    st.subheader("🔮 Predicción de flujo de caja")
    pred = predecir(df)
    st.write(pred).     from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
import numpy as np

def detectar_anomalias(df):
    model = IsolationForest(contamination=0.2, random_state=42)
    X = df[["ingresos", "gastos"]]
    model.fit(X)
    return model.predict(X)

def predecir(df):
    X = df[["mes"]]
    y = df["ingresos"] - df["gastos"]

    model = LinearRegression()
    model.fit(X, y)

    futuro = np.array([[df["mes"].max() + 1]])
    pred = model.predict(futuro)

    return {"flujo_predicho": float(pred[0])}.        def limpiar_datos(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df.              mes,ingresos,gastos
1,1000,800
2,1200,900
3,900,850
4,1500,1000
5,1300,950.           streamlit
pandas
numpy
scikit-learn.    b   