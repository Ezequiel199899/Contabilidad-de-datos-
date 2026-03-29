mkdir ai
cd ai

mkdir app models utils data

type nul > app/app.py
type nul > models/model.py
type nul > utils/preprocessing.py
type nul > data/sample_data.csv
type nul > requirements.txt
type nul > README.md                                                       mkdir ai
cd ai

mkdir app models utils data

type nul > app/app.py
type nul > models/model.py
type nul > utils/preprocessing.py
type nul > data/sample_data.csv
type nul > requirements.txt
type nul > README.md                     import streamlit as st
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
    st.write(pred)                     def limpiar_datos(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df                   streamlit run app/app.py           type nul > app/__init__.py
type nul > models/__init__.py
type nul > utils/__init__.py      m                                                                         
