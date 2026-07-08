import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import plotly.express as px

st.set_page_config(
    page_title="Perbandingan Model",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Perbandingan Model")

st.markdown("""
Tahap ini membandingkan performa algoritma **Multiple Linear Regression**
dan **Random Forest Regression** menggunakan metrik evaluasi yang sama.
""")

st.divider()

# ==========================
# LOAD DATA
# ==========================

df = pd.read_excel("data/dataset_daging_sapi_2021_2025.xlsx")

df = df.dropna()

X = df[
    [
        "Lag_1",
        "Lag_2",
        "Indeks_Pakan",
        "Indikator_Lebaran"
    ]
]

y = df["Harga"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=False
)

# ==========================
# MLR
# ==========================

mlr = LinearRegression()
mlr.fit(X_train, y_train)

pred_mlr = mlr.predict(X_test)

# ==========================
# RANDOM FOREST
# ==========================

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

# ==========================
# FUNGSI METRIK
# ==========================

def hitung(y_true, y_pred):

    mae = mean_absolute_error(y_true, y_pred)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))

    mape = np.mean(
        np.abs((y_true - y_pred) / y_true)
    ) * 100

    r2 = r2_score(y_true, y_pred)

    return mae, rmse, mape, r2

mlr_mae, mlr_rmse, mlr_mape, mlr_r2 = hitung(y_test, pred_mlr)

rf_mae, rf_rmse, rf_mape, rf_r2 = hitung(y_test, pred_rf)

# ==========================
# TABEL
# ==========================

hasil = pd.DataFrame({

    "Model":[
        "Multiple Linear Regression",
        "Random Forest"
    ],

    "MAE":[
        mlr_mae,
        rf_mae
    ],

    "RMSE":[
        mlr_rmse,
        rf_rmse
    ],

    "MAPE (%)":[
        mlr_mape,
        rf_mape
    ],

    "R²":[
        mlr_r2,
        rf_r2
    ]

})

st.subheader("📋 Hasil Perbandingan")

st.dataframe(
    hasil.round(3),
    use_container_width=True
)

st.divider()

# ==========================
# BAR CHART
# ==========================

st.subheader("📊 Perbandingan Nilai MAE")

fig = px.bar(
    hasil,
    x="Model",
    y="MAE",
    color="Model",
    text="MAE"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📊 Perbandingan Nilai RMSE")

fig = px.bar(
    hasil,
    x="Model",
    y="RMSE",
    color="Model",
    text="RMSE"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📊 Perbandingan Nilai MAPE")

fig = px.bar(
    hasil,
    x="Model",
    y="MAPE (%)",
    color="Model",
    text="MAPE (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📊 Perbandingan Nilai R²")

fig = px.bar(
    hasil,
    x="Model",
    y="R²",
    color="Model",
    text="R²"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================
# KESIMPULAN
# ==========================

terbaik = hasil.loc[hasil["RMSE"].idxmin(), "Model"]

st.success(f"""
### Kesimpulan

Berdasarkan hasil pengujian:

- Model dengan **RMSE terkecil** adalah **{terbaik}**.
- Nilai MAE dan MAPE digunakan untuk melihat besar kesalahan prediksi.
- Nilai R² digunakan untuk melihat kemampuan model dalam menjelaskan variasi data.

Model dengan performa terbaik dapat dipilih sebagai model yang digunakan pada tahap deployment.
""")