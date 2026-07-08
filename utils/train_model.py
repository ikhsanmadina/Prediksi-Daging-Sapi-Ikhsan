import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression

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

# ==========================
# TRAIN MODEL
# ==========================

model = LinearRegression()

model.fit(X, y)

# ==========================
# SIMPAN MODEL
# ==========================

joblib.dump(
    model,
    "models/model_mlr.pkl"
)

print("Model berhasil disimpan.")