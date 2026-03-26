 data/
notebooks/
src/
reports/.  import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def basic_analysis(df):
    print("Resumen del dataset:")
    print(df.describe())

def detect_anomalies(df, column):
    threshold = df[column].mean() + 2 * df[column].std()
    anomalies = df[df[column] > threshold]
    return anomalies

if __name__ == "__main__":
    df = load_data("../data/financial_data.csv")
    basic_analysis(df)

    anomalies = detect_anomalies(df, "expenses")
    print("\nAnomalías detectadas:")
    print(anomalies).    date,income,expenses
2024-01-01,1000,800
2024-01-02,1200,900
2024-01-03,1100,950
2024-01-04,1300,2000
2024-01-05,1250,870
2024-01-06,1400,920
2024-01-07,1500,3000.         import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/financial_data.csv")

df.plot(x="date", y=["income", "expenses"])
plt.xticks(rotation=45)
plt.show().         plt.savefig("../reports/financial_plot.png").       pandas
matplotlib
numpy
seaborn.     pip install -r requirements.txt
python src/analysis.py. import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(df):
    df = df.copy()
    df["day"] = range(len(df))

    X = df[["day"]]
    y = df["expenses"]

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_future(model, last_day, days_ahead=3):
    future_days = [[last_day + i] for i in range(1, days_ahead + 1)]
    predictions = model.predict(future_days)
    return predictions scikit-learn.   scikit-learn.     pandas
matplotlib
numpy
seaborn
scikit-learn
streamlit.   from src.model import train_model, predict_future.    # Predicción
st.subheader("🔮 Predicción de gastos futuros")

model = train_model(df)
preds = predict_future(model, len(df))

st.write("Próximos gastos estimados:")
st.write(preds). pip install -r requirements.txt
streamlit run app.py      