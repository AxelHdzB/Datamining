import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV de ventas de videojuegos
df = pd.read_csv("vgchartz-2024.csv")

# Seleccionar solo columnas numéricas para calcular la matriz de correlación
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))

# Mapa de calor de la matriz de correlación
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

plt.title('Matriz de correlación de ventas de videojuegos')
plt.show()

# Gráfico de dispersión con regresión lineal
plt.scatter(df['critic_score'], df['total_sales'], alpha=0.5)
sns.regplot(x='critic_score', y='total_sales', data=df, scatter=False, color='red', line_kws={"color":"red"})

plt.xlabel('Puntuación de los críticos')
plt.ylabel('Ventas totales')
plt.title('Regresión lineal de Puntuación de Críticos | Ventas Totales')

plt.show()
