import streamlit as st

st.set_page_config(
    page_title="Prediksi Harga Daging Sapi",
    page_icon="🥩",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main{
    background:#F8FAFC;
}

.block-container{
    padding-top:2rem;
}

.big-font{
font-size:45px;
font-weight:bold;
color:#1E3A8A;
}

.subtitle{
font-size:20px;
color:#555;
}

.metric-card{
padding:20px;
border-radius:15px;
background:white;
box-shadow:0px 3px 12px rgba(0,0,0,.15);
text-align:center;
}

.footer{
text-align:center;
padding:30px;
font-size:14px;
color:gray;
}

</style>
""", unsafe_allow_html=True)

st.title("🥩 Prediksi Harga Daging Sapi Kota Sukabumi")

st.markdown("""
### Multiple Linear Regression

Dashboard implementasi penelitian skripsi menggunakan metode **CRISP-DM**
untuk memprediksi harga daging sapi di Kota Sukabumi
berdasarkan data historis SIPANDA Tahun 2021–2025.
""")

st.divider()

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric(
        "📅 Periode Data",
        "2021-2025"
    )

with col2:
    st.metric(
        "🤖 Algoritma",
        "MLR"
    )

with col3:
    st.metric(
        "📊 Framework",
        "CRISP-DM"
    )

with col4:
    st.metric(
        "📍 Lokasi",
        "Sukabumi"
    )

st.divider()

st.header("Tentang Aplikasi")

st.write("""
Aplikasi ini dibuat sebagai implementasi hasil penelitian skripsi:

**Prediksi Harga Daging Sapi di Kota Sukabumi
Menggunakan Algoritma Multiple Linear Regression**

Seluruh proses mengikuti tahapan:

- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment

Silakan gunakan menu di sebelah kiri untuk melihat setiap tahapan penelitian.
""")

st.info("➡️ Mulai dari menu Business Understanding pada sidebar.")