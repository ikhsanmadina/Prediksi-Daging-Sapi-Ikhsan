import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import plotly.express as px

st.set_page_config(
    page_title="Evaluasi",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Evaluasi Model")

st.markdown("""
Tahap evaluasi dilakukan untuk mengetahui tingkat akurasi model
Multiple Linear Regression menggunakan beberapa metrik evaluasi.
""")

st.divider()

# =======================================================
# LOAD DATA
# =======================================================

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

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    shuffle=False,
    random_state=42
)

model = LinearRegression()

model.fit(X_train,y_train)

pred = model.predict(X_test)

# =======================================================
# METRIK
# =======================================================

mae = mean_absolute_error(y_test,pred)

mse = mean_squared_error(y_test,pred)

rmse = np.sqrt(mse)

mape = np.mean(
    np.abs((y_test-pred)/y_test)
)*100

r2 = r2_score(y_test,pred)

# =======================================================
# KPI
# =======================================================

st.header("📌 Hasil Evaluasi")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "MAE",
    f"{mae:,.2f}"
)

c2.metric(
    "RMSE",
    f"{rmse:,.2f}"
)

c3.metric(
    "MAPE",
    f"{mape:.2f}%"
)

c4.metric(
    "R²",
    f"{r2:.4f}"
)

st.divider()

# =======================================================
# GRAFIK
# =======================================================

hasil = pd.DataFrame({
    "Aktual":y_test.values,
    "Prediksi":pred
})

st.subheader("📈 Aktual vs Prediksi")

fig = px.line(
    hasil.head(100),
    y=["Aktual","Prediksi"],
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =======================================================
# SCATTER
# =======================================================

st.subheader("🎯 Scatter Plot")

fig = px.scatter(
    hasil,
    x="Aktual",
    y="Prediksi",
    trendline="ols"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =======================================================
# ERROR
# =======================================================

hasil["Error"] = hasil["Aktual"]-hasil["Prediksi"]

st.subheader("📉 Distribusi Error")

fig = px.histogram(
    hasil,
    x="Error",
    nbins=30
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =======================================================
# INTERPRETASI
# =======================================================

st.header("📝 Interpretasi Hasil")

interpretasi = pd.DataFrame({
    "Metrik":[
        "MAE",
        "RMSE",
        "MAPE",
        "R² Score"
    ],
    "Nilai":[
        round(mae,2),
        round(rmse,2),
        round(mape,2),
        round(r2,4)
    ],
    "Interpretasi":[
        "Rata-rata kesalahan absolut prediksi.",
        "Kesalahan prediksi berbobot.",
        "Persentase rata-rata kesalahan prediksi.",
        "Kemampuan model menjelaskan variasi data."
    ]
})

st.dataframe(
    interpretasi,
    use_container_width=True
)

st.divider()

# =======================================================
# KESIMPULAN
# =======================================================

st.success(f"""
### Kesimpulan

Model Multiple Linear Regression berhasil melakukan prediksi harga
daging sapi menggunakan empat variabel prediktor.

Nilai evaluasi model diperoleh sebagai berikut:

• MAE : {mae:,.2f}

• RMSE : {rmse:,.2f}

• MAPE : {mape:.2f}%

• R² Score : {r2:.4f}

Semakin kecil nilai MAE, RMSE, dan MAPE,
maka semakin baik performa model dalam melakukan prediksi.
""")