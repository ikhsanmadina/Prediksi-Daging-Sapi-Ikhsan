import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Modeling",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Modeling")

st.markdown("""
Tahap **Modeling** bertujuan membangun model prediksi harga daging sapi
menggunakan algoritma **Multiple Linear Regression**.
""")

st.divider()

# =========================================
# LOAD DATA
# =========================================

df = pd.read_excel("data/dataset_daging_sapi_2021_2025.xlsx")

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

# Menghapus missing value
df = df.dropna()

# =========================================
# FEATURE & TARGET
# =========================================

X = df[[
    "Lag_1",
    "Lag_2",
    "Indeks_Pakan",
    "Indikator_Lebaran"
]]

y = df["Harga"]

# =========================================
# TRAIN TEST SPLIT
# =========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=False
)

# =========================================
# TRAIN MODEL
# =========================================

model = LinearRegression()

model.fit(X_train, y_train)

# =========================================
# HASIL MODEL
# =========================================

st.header("📊 Informasi Model")

c1, c2, c3 = st.columns(3)

c1.metric("Training Data", len(X_train))
c2.metric("Testing Data", len(X_test))
c3.metric("Jumlah Variabel", X.shape[1])

st.divider()

# =========================================
# INTERCEPT
# =========================================

st.subheader("📍 Intercept")

st.success(f"{model.intercept_:,.4f}")

st.divider()

# =========================================
# KOEFISIEN
# =========================================

st.subheader("📈 Koefisien Regresi")

coef = pd.DataFrame({
    "Variabel": X.columns,
    "Koefisien": model.coef_
})

st.dataframe(
    coef,
    use_container_width=True
)

fig = px.bar(
    coef,
    x="Variabel",
    y="Koefisien",
    text="Koefisien",
    color="Koefisien"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =========================================
# PERSAMAAN
# =========================================

st.subheader("🧮 Persamaan Regresi")

equation = f"""
Harga =
{model.intercept_:.2f}
"""

for i, col in enumerate(X.columns):

    equation += f"""
+ ({model.coef_[i]:.4f} × {col})
"""

st.code(equation)

st.divider()

# =========================================
# PREDIKSI
# =========================================

st.subheader("📉 Hasil Prediksi")

prediksi = model.predict(X_test)

hasil = pd.DataFrame({
    "Aktual": y_test.values,
    "Prediksi": prediksi
})

st.dataframe(
    hasil.head(20),
    use_container_width=True
)

fig = px.line(
    hasil.head(100)
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.success("""
### Kesimpulan

Model Multiple Linear Regression berhasil dibangun menggunakan
empat variabel prediktor:

- Lag_1
- Lag_2
- Indeks_Pakan
- Indikator_Lebaran

Selanjutnya model akan dievaluasi menggunakan
MAE, RMSE, dan MAPE.
""")