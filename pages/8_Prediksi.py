import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediksi Harga",
    page_icon="💰",
    layout="wide"
)

# ===========================
# LOAD MODEL
# ===========================

model = joblib.load("models/model_mlr.pkl")

# ===========================
# HEADER
# ===========================

st.title("💰 Prediksi Harga Daging Sapi")

st.markdown("""
Halaman ini digunakan untuk melakukan prediksi harga daging sapi
menggunakan model **Multiple Linear Regression** yang telah dilatih.
Silakan masukkan nilai variabel prediktor di bawah ini.
""")

st.divider()

# ===========================
# INPUT
# ===========================

st.subheader("📥 Input Variabel")

col1, col2 = st.columns(2)

with col1:
    lag1 = st.number_input(
        "Harga Hari Sebelumnya (Lag_1)",
        min_value=0.0,
        value=120000.0,
        step=100.0
    )

    lag2 = st.number_input(
        "Harga Dua Hari Sebelumnya (Lag_2)",
        min_value=0.0,
        value=120000.0,
        step=100.0
    )

with col2:
    indeks = st.number_input(
        "Indeks Pakan",
        min_value=0.000,
        value=1.000,
        step=0.001,
        format="%.3f"
    )

    lebaran = st.selectbox(
        "Indikator Lebaran",
        options=[0, 1],
        format_func=lambda x: "Ya" if x == 1 else "Tidak"
    )

st.divider()

# ===========================
# BUTTON PREDIKSI
# ===========================

if st.button("🔍 Prediksi Harga", use_container_width=True):

    data = pd.DataFrame({
        "Lag_1": [lag1],
        "Lag_2": [lag2],
        "Indeks_Pakan": [indeks],
        "Indikator_Lebaran": [lebaran]
    })

    hasil = model.predict(data)[0]

    selisih = hasil - lag1
    persentase = (selisih / lag1) * 100 if lag1 != 0 else 0

    st.success("✅ Prediksi berhasil dilakukan.")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            label="💰 Prediksi Harga",
            value=f"Rp {hasil:,.2f}",
            delta=f"{selisih:,.2f}"
        )

    with c2:
        st.metric(
            label="📊 Persentase Perubahan",
            value=f"{persentase:.2f}%"
        )

    st.divider()

    # ===========================
    # INTERPRETASI
    # ===========================

    if hasil > lag1:

        st.success(f"""
### 📈 Prediksi Harga Naik

Harga daging sapi diperkirakan **NAIK**
dibandingkan harga hari sebelumnya.

- Kenaikan Harga : **Rp {selisih:,.2f}**
- Persentase Kenaikan : **{persentase:.2f}%**
""")

    elif hasil < lag1:

        st.error(f"""
### 📉 Prediksi Harga Turun

Harga daging sapi diperkirakan **TURUN**
dibandingkan harga hari sebelumnya.

- Penurunan Harga : **Rp {abs(selisih):,.2f}**
- Persentase Penurunan : **{abs(persentase):.2f}%**
""")

    else:

        st.info("""
### ➖ Prediksi Harga Tetap

Harga diperkirakan tidak mengalami perubahan
dibandingkan hari sebelumnya.
""")

    st.divider()

    # ===========================
    # RINGKASAN INPUT
    # ===========================

    st.subheader("📋 Ringkasan Data Input")

    tampil = pd.DataFrame({
        "Variabel": [
            "Lag_1",
            "Lag_2",
            "Indeks_Pakan",
            "Indikator_Lebaran"
        ],
        "Nilai": [
            lag1,
            lag2,
            indeks,
            "Ya" if lebaran == 1 else "Tidak"
        ]
    })

    st.dataframe(
        tampil,
        use_container_width=True
    )

    st.info("""
Interpretasi:

Prediksi dihasilkan menggunakan model **Multiple Linear Regression**
yang telah dibangun dari dataset historis harga daging sapi Kota Sukabumi.
Hasil prediksi dapat digunakan sebagai estimasi harga berdasarkan kondisi
variabel yang dimasukkan oleh pengguna.
""")