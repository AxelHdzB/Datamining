import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# Cargar el archivo CSV localmente
df = pd.read_csv("vgchartz-2024.csv")

# KMeans con k=3
kmeans = KMeans(n_clusters=3)

# Manejar valores faltantes
imputer = SimpleImputer(strategy="mean")
df[["total_sales", "na_sales", "jp_sales", "pal_sales", "other_sales"]] = imputer.fit_transform(df[["total_sales", "na_sales", "jp_sales", "pal_sales", "other_sales"]])

# Seleccionar las características relevantes para el clustering (ventas totales, ventas en NA, ventas en Japón, ventas en PAL y ventas en otros países)
X = df[["total_sales", "na_sales", "jp_sales", "pal_sales", "other_sales"]]

# Aplicar KMeans
kmeans.fit(X)

# Obtener los clusters
clusters = kmeans.predict(X)

# Agregar la columna 'Grupo' al DataFrame original
df['Grupo'] = clusters

# Graficar
plt.figure(figsize=(10, 6))

for cluster in df['Grupo'].unique():
    cluster_df = df[df['Grupo'] == cluster]
    plt.scatter(cluster_df.index, cluster_df['total_sales'], label=f'Grupo {cluster}')

plt.title('Clustering de Ventas de Videojuegos')
plt.xlabel('Índice del juego')
plt.ylabel('Ventas totales')
plt.legend()
plt.grid(True)
plt.show()
