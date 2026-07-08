import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.stattools import durbin_watson

st.set_page_config(
    page_title="Uji Asumsi",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Uji Asumsi Klasik")

st.markdown("""
Tahap ini bertujuan memastikan model Multiple Linear Regression
memenuhi asumsi-asumsi statistik sebelum dilakukan evaluasi.
""")

st.divider()

# =======================================================
# LOAD DATA
# =======================================================

df = pd.read_excel("data/dataset_daging_sapi_2021_2025.xlsx")

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

df = df.dropna()

X = df[[
    "Lag_1",
    "Lag_2",
    "Indeks_Pakan",
    "Indikator_Lebaran"
]]

y = df["Harga"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=False
)

model = LinearRegression()

model.fit(X_train,y_train)

pred = model.predict(X_test)

residual = y_test - pred

# =======================================================
# NORMALITAS
# =======================================================

st.header("1️⃣ Uji Normalitas Residual")

fig = px.histogram(
    residual,
    nbins=30,
    title="Distribusi Residual"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("""
Residual yang menyebar mendekati distribusi normal menunjukkan
bahwa asumsi normalitas telah terpenuhi.
""")

st.divider()

# =======================================================
# MULTIKOLINEARITAS
# =======================================================

st.header("2️⃣ Uji Multikolinearitas (VIF)")

X_vif = sm.add_constant(X)

vif = pd.DataFrame()

vif["Variabel"] = X_vif.columns

vif["VIF"] = [
    variance_inflation_factor(X_vif.values,i)
    for i in range(X_vif.shape[1])
]

st.dataframe(
    vif,
    use_container_width=True
)

fig = px.bar(
    vif,
    x="Variabel",
    y="VIF",
    text="VIF"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("""
Nilai VIF < 10 menunjukkan tidak terjadi multikolinearitas.
""")

st.divider()

# =======================================================
# HETEROSKEDASTISITAS
# =======================================================

st.header("3️⃣ Uji Heteroskedastisitas")

scatter = pd.DataFrame({
    "Prediksi":pred,
    "Residual":residual
})

fig = px.scatter(
    scatter,
    x="Prediksi",
    y="Residual",
    trendline="ols"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info("""
Residual yang menyebar secara acak menunjukkan
tidak terjadi heteroskedastisitas.
""")

st.divider()

# =======================================================
# DURBIN WATSON
# =======================================================

st.header("4️⃣ Uji Autokorelasi")

dw = durbin_watson(residual)

st.metric(
    "Nilai Durbin-Watson",
    f"{dw:.3f}"
)

if 1.5 <= dw <= 2.5:
    st.success("Tidak terdapat autokorelasi.")
else:
    st.warning("Perlu dilakukan analisis lebih lanjut.")

st.divider()

# =======================================================
# KESIMPULAN
# =======================================================

st.success(f"""
## Kesimpulan Uji Asumsi

✅ Normalitas residual telah dianalisis.

✅ Nilai Durbin-Watson = **{dw:.3f}**

✅ Multikolinearitas diuji menggunakan VIF.

✅ Heteroskedastisitas dianalisis melalui scatter plot residual.

Model siap memasuki tahap **Evaluasi**.
""")