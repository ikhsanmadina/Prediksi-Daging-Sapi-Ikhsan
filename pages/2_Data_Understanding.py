import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================
# CONFIG
# ==========================

st.set_page_config(
    page_title="Data Understanding",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Understanding")

st.markdown("""
Tahap **Data Understanding** bertujuan memahami karakteristik dataset,
mengidentifikasi kualitas data, serta memperoleh gambaran awal sebelum
memasuki proses **Data Preparation**.
""")

st.divider()

# ==========================
# KELOLA DATASET
# ==========================

DEFAULT_PATH = "data/dataset_daging_sapi_2021_2025.xlsx"

if "dataset" not in st.session_state:
    st.session_state["dataset"] = pd.read_excel(DEFAULT_PATH)
    st.session_state["nama_file"] = "dataset_daging_sapi_2021_2025.xlsx"

st.subheader("📂 Kelola Dataset")

uploaded_file = st.file_uploader(
    "Upload Dataset (.xlsx)",
    type=["xlsx"]
)

if uploaded_file is not None:
    st.session_state["dataset"] = pd.read_excel(uploaded_file)
    st.session_state["nama_file"] = uploaded_file.name
    st.success(f"✅ Dataset **{uploaded_file.name}** berhasil diupload.")

df = st.session_state["dataset"].copy()

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

col1, col2, col3 = st.columns(3)

col1.metric("📄 Nama File", st.session_state["nama_file"])
col2.metric("📊 Jumlah Baris", len(df))
col3.metric("📋 Jumlah Kolom", len(df.columns))

st.divider()

kolom_wajib = [
    "Tanggal",
    "Harga",
    "Lag_1",
    "Lag_2",
    "Indikator_Lebaran",
    "Indeks_Pakan"
]

kolom_tidak_ada = [
    k for k in kolom_wajib if k not in df.columns
]

if kolom_tidak_ada:
    st.error(f"Kolom berikut belum tersedia: {kolom_tidak_ada}")
    st.stop()

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

st.subheader("✏️ Edit Dataset")



col1, col2, col3 = st.columns(3)

col1.metric("📄 Nama File", st.session_state["nama_file"])
col2.metric("📊 Jumlah Baris", len(df))
col3.metric("📋 Jumlah Kolom", len(df.columns))

# ==========================
# PENGECEKAN MISSING VALUE
# ==========================

st.subheader("Pengecekan Missing Value")

st.write(df.isnull().sum())

st.write(df[df.isnull().any(axis=1)])

# ==========================
# KPI
# ==========================

harga_mean = df["Harga"].mean()
harga_max = df["Harga"].max()
harga_min = df["Harga"].min()

c1,c2,c3,c4 = st.columns(4)

periode_awal = df["Tanggal"].dt.year.min()
periode_akhir = df["Tanggal"].dt.year.max()

c1.metric(
    "📅 Periode",
    f"{periode_awal}-{periode_akhir}"
)

c2.metric(
    "📊 Jumlah Data",
    len(df)
)

c3.metric(
    "🥩 Harga Rata-rata",
    f"Rp {harga_mean:,.0f}"
)

c4.metric(
    "❗ Missing Value",
    int(df.isnull().sum().sum())
)

st.divider()

# ==========================
# PREVIEW
# ==========================

st.subheader("👀 Preview Dataset")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.divider()

# ==========================
# STRUKTUR DATA
# ==========================

st.subheader("📋 Struktur Dataset")

struktur = pd.DataFrame({
    "Kolom":df.columns,
    "Tipe Data":df.dtypes.astype(str),
    "Missing":df.isnull().sum().values
})

st.dataframe(
    struktur,
    use_container_width=True
)

st.divider()

# ==========================
# TREND HARGA
# ==========================

st.subheader("📈 Trend Harga Daging Sapi")

fig = px.line(
    df,
    x="Tanggal",
    y="Harga",
    markers=True
)

fig.update_layout(
    height=500,
    xaxis_title="Tanggal",
    yaxis_title="Harga"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================
# HISTOGRAM
# ==========================

col1,col2 = st.columns(2)

with col1:

    st.subheader("📊 Distribusi Harga")

    fig = px.histogram(
        df,
        x="Harga",
        nbins=30
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("📦 Boxplot Harga")

    fig = px.box(
        df,
        y="Harga"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================
# KORELASI
# ==========================

st.subheader("🔥 Korelasi Antar Variabel")

corr = df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    aspect="auto"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================
# STATISTIK
# ==========================

st.subheader("📑 Statistik Deskriptif")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# ==========================
# INSIGHT
# ==========================

st.success(f"""

### 💡 Insight Dataset

✅ Jumlah data : **{len(df)}**

✅ Jumlah atribut : **{len(df.columns)}**

✅ Harga rata-rata : **Rp {harga_mean:,.0f}**

✅ Harga tertinggi : **Rp {harga_max:,.0f}**

✅ Harga terendah : **Rp {harga_min:,.0f}**

✅ Missing Value : **{int(df.isnull().sum().sum())}**

Dataset telah dipahami dengan baik dan siap memasuki tahap **Data Preparation**.
""")