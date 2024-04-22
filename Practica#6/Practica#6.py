import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA

# Leer el archivo CSV
df = pd.read_csv("vgchartz-2024.csv")

# Manejar valores faltantes
imputer = SimpleImputer(strategy="mean")
df[["critic_score", "total_sales"]] = imputer.fit_transform(df[["critic_score", "total_sales"]])

# Escalar los datos
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[["critic_score", "total_sales"]])

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df["Exito"] = kmeans.fit_predict(scaled_data)

# Visualizar los resultados
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)
df["PC1"] = principal_components[:, 0]
df["PC2"] = principal_components[:, 1]

plt.figure(figsize=(10, 6))
for cluster in df["Exito"].unique():
    plt.scatter(df[df["Exito"] == cluster]["PC1"], df[df["Exito"] == cluster]["PC2"], label=f"Exito {cluster}")

plt.xlabel("Desempeño")
plt.ylabel("Recepcion Critica")
plt.title("Clasificación de Videojuegos por Ventas y Puntuaciones de Críticos")
plt.legend()
plt.grid(True)
plt.show()
