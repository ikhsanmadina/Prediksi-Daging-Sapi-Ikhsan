import streamlit as st

st.set_page_config(page_title="Business Understanding", layout="wide")

st.title("📊 Business Understanding")
st.markdown("Tahapan pertama dalam metodologi **CRISP-DM** untuk memahami permasalahan bisnis dan menentukan tujuan penelitian.")

st.divider()

col1, col2 = st.columns([1,1])

with col1:
    st.error("### Permasalahan")

    st.markdown("""
- Terjadi **fluktuasi harga daging sapi** di Kota Sukabumi.
- Harga cenderung meningkat menjelang **Hari Raya Idul Fitri**.
- Pemerintah masih menggunakan data SIPANDA untuk **monitoring**, belum untuk prediksi.
- Belum tersedia sistem yang mampu memberikan **prediksi harga** sebagai pendukung pengambilan keputusan.
""")

with col2:
    st.success("### Tujuan Penelitian")

    st.markdown("""
- Membangun model prediksi harga daging sapi.
- Menggunakan algoritma **Multiple Linear Regression**.
- Mengimplementasikan tahapan **CRISP-DM**.
- Menghasilkan prediksi yang dapat membantu pemerintah mengantisipasi kenaikan harga.
""")

st.divider()

st.subheader("📌 Faktor yang Mempengaruhi Harga")

c1,c2,c3=st.columns(3)

with c1:
    st.info("""
### 📈 Harga Historis

Perubahan harga pada periode sebelumnya
digunakan sebagai dasar prediksi harga berikutnya.
""")

with c2:
    st.warning("""
### 🕌 Momentum Idul Fitri

Permintaan masyarakat meningkat
menjelang Hari Raya sehingga
harga cenderung naik.
""")

with c3:
    st.success("""
### 🌾 Harga Pakan

Perubahan harga pakan
mempengaruhi biaya produksi
peternak sehingga berdampak
pada harga daging sapi.
""")

st.divider()

st.subheader("🎯 Solusi Penelitian")





st.text("""
Permasalahan
      │
      ▼
Pengumpulan Data SIPANDA
      │
      ▼
Feature Engineering
      │
      ▼
Multiple Linear Regression
      │
      ▼
Evaluasi (MAE, RMSE, MAPE)
      │
      ▼
Prediksi Harga Daging Sapi
""")