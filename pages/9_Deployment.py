import streamlit as st

st.set_page_config(
    page_title="Deployment",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Deployment")

st.markdown("""
Tahap **Deployment** merupakan tahap akhir dalam metodologi **CRISP-DM**.
Pada tahap ini model **Multiple Linear Regression** yang telah dibangun
berhasil diimplementasikan ke dalam aplikasi berbasis **Streamlit**
sehingga dapat digunakan untuk melakukan prediksi harga daging sapi.
""")

st.divider()

# ==================================================
# STATUS IMPLEMENTASI
# ==================================================

st.header("✅ Status Implementasi")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Model",
    "MLR"
)

c2.metric(
    "Dataset",
    "1826 Data"
)

c3.metric(
    "Framework",
    "Streamlit"
)

c4.metric(
    "Status",
    "Deploy Ready"
)

st.divider()

# ==================================================
# TEKNOLOGI
# ==================================================

st.header("🛠️ Teknologi yang Digunakan")

tech = [
    "🐍 Python 3",
    "📊 Pandas",
    "🤖 Scikit-Learn",
    "📈 Plotly",
    "🌐 Streamlit",
    "📁 Joblib"
]

for item in tech:
    st.write(item)

st.divider()

# ==================================================
# FITUR
# ==================================================

st.header("✨ Fitur Aplikasi")

fitur = [
    "Business Understanding",
    "Data Understanding",
    "Data Preparation",
    "Modeling",
    "Uji Asumsi Klasik",
    "Evaluasi Model",
    "Perbandingan Model",
    "Prediksi Harga Daging Sapi"
]

for i, f in enumerate(fitur, start=1):
    st.write(f"{i}. {f}")

st.divider()

# ==================================================
# ALUR SISTEM
# ==================================================

st.header("🔄 Alur Implementasi")

st.code("""
Dataset SIPANDA
        │
        ▼
Data Understanding
        │
        ▼
Data Preparation
        │
        ▼
Modeling (Multiple Linear Regression)
        │
        ▼
Evaluasi Model
        │
        ▼
Model Disimpan (.pkl)
        │
        ▼
Aplikasi Streamlit
        │
        ▼
Prediksi Harga Daging Sapi
""")

st.divider()

# ==================================================
# MANFAAT
# ==================================================

st.header("🎯 Manfaat Aplikasi")

st.markdown("""
Aplikasi ini dikembangkan sebagai implementasi hasil penelitian untuk:

- Membantu memprediksi harga daging sapi berdasarkan data historis.
- Mendukung proses pengambilan keputusan.
- Memberikan estimasi harga yang lebih cepat.
- Menjadi media visualisasi hasil penelitian.
- Mengimplementasikan metode CRISP-DM dalam bentuk aplikasi web.
""")

st.divider()

# ==================================================
# KESIMPULAN
# ==================================================

st.success("""
## Kesimpulan

Model **Multiple Linear Regression** telah berhasil diimplementasikan
ke dalam aplikasi berbasis **Streamlit**.

Seluruh tahapan penelitian mulai dari **Business Understanding,
Data Understanding, Data Preparation, Modeling,
Uji Asumsi, Evaluasi, Perbandingan Model,
hingga Prediksi** telah berhasil diintegrasikan
ke dalam satu aplikasi yang dapat digunakan
untuk melakukan prediksi harga daging sapi secara interaktif.
""")

st.balloons()