import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Preparation",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Data Preparation")

st.markdown("""
Tahap **Data Preparation** bertujuan menyiapkan dataset sebelum proses
pemodelan Multiple Linear Regression dilakukan.
""")

st.divider()

# ====================================
# LOAD DATA
# ====================================

df = pd.read_excel("data/dataset_daging_sapi_2021_2025.xlsx")

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

# ====================================
# SEBELUM PREPROCESSING
# ====================================

st.header("📋 Dataset Sebelum Preprocessing")

c1,c2,c3 = st.columns(3)

c1.metric(
    "Jumlah Data",
    len(df)
)

c2.metric(
    "Jumlah Kolom",
    len(df.columns)
)

c3.metric(
    "Missing Value",
    int(df.isnull().sum().sum())
)

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# ====================================
# MISSING VALUE
# ====================================

st.header("🔍 Pengecekan Missing Value")

missing = pd.DataFrame({
    "Kolom": df.columns,
    "Jumlah Missing": df.isnull().sum().values
})

st.dataframe(
    missing,
    use_container_width=True
)

fig = px.bar(
    missing,
    x="Kolom",
    y="Jumlah Missing",
    text="Jumlah Missing",
    title="Missing Value Sebelum Preprocessing"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ====================================
# PREPROCESSING
# ====================================

st.header("⚙️ Proses Preprocessing")

st.markdown("""
Tahapan preprocessing yang dilakukan meliputi:

- Konversi kolom **Tanggal** ke format datetime.
- Menghapus data yang memiliki **missing value**.
- Memastikan seluruh variabel numerik siap digunakan.
""")

df_clean = df.dropna().copy()

st.success("✅ Missing Value berhasil dihapus menggunakan dropna().")

st.divider()

# ====================================
# SETELAH PREPROCESSING
# ====================================

st.header("✅ Dataset Setelah Preprocessing")

c1,c2,c3 = st.columns(3)

c1.metric(
    "Jumlah Data",
    len(df_clean)
)

c2.metric(
    "Jumlah Kolom",
    len(df_clean.columns)
)

c3.metric(
    "Missing Value",
    int(df_clean.isnull().sum().sum())
)

st.dataframe(
    df_clean.head(10),
    use_container_width=True
)

st.divider()

# ====================================
# TRAIN TEST SPLIT
# ====================================

st.header("📊 Pembagian Data")

train = int(len(df_clean) * 0.8)
test = len(df_clean) - train

c1,c2 = st.columns(2)

c1.metric(
    "Training Data (80%)",
    train
)

c2.metric(
    "Testing Data (20%)",
    test
)

split = pd.DataFrame({
    "Kategori":["Training","Testing"],
    "Jumlah":[train,test]
})

fig = px.pie(
    split,
    values="Jumlah",
    names="Kategori",
    hole=.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ====================================
# FITUR YANG DIGUNAKAN
# ====================================

st.header("📑 Variabel Penelitian")

fitur = pd.DataFrame({
    "Variabel":[
        "Lag_1",
        "Lag_2",
        "Indeks_Pakan",
        "Indikator_Lebaran"
    ],
    "Jenis":[
        "Prediktor",
        "Prediktor",
        "Prediktor",
        "Prediktor"
    ]
})

st.dataframe(
    fitur,
    use_container_width=True
)

st.info("""
Variabel target yang akan diprediksi adalah:

### Harga
""")

st.divider()

# ====================================
# KESIMPULAN
# ====================================

st.success(f"""
## Kesimpulan Data Preparation

✅ Dataset awal : **{len(df)}** data

✅ Dataset setelah preprocessing : **{len(df_clean)}** data

✅ Missing Value sebelum preprocessing : **3**

✅ Missing Value setelah preprocessing : **0**

Dataset telah siap digunakan pada tahap **Modeling** menggunakan
algoritma **Multiple Linear Regression**.
""")