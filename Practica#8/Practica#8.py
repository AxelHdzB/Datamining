import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Leer el archivo CSV de ventas de videojuegos
df = pd.read_csv("vgchartz-2024.csv")

# Manejar valores faltantes
imputer = SimpleImputer(strategy="mean")
df[["total_sales", "critic_score"]] = imputer.fit_transform(df[["total_sales", "critic_score"]])

# Entrenar el modelo de regresión lineal
model = LinearRegression()
X = df[['critic_score']]  # Puntuación de los críticos como variable independiente
y = df['total_sales']     # Ventas totales como variable dependiente
model.fit(X, y)

# Pronosticar las ventas futuras para una nueva puntuación de críticos (por ejemplo, 9.0)
new_critic_score = 9.0
future_sales = model.predict([[new_critic_score]])

# Imprimir el pronóstico
print("Pronóstico de ventas futuras para una puntuación de críticos de", new_critic_score, ":", future_sales[0])

# Graficar los datos y la línea de regresión
plt.scatter(X, y, color='blue', label='Datos')
plt.plot(X, model.predict(X), color='red', label='Regresión Lineal')
plt.scatter(new_critic_score, future_sales, color='green', label='Pronóstico')
plt.xlabel('Puntuación de los Críticos')
plt.ylabel('Ventas Totales')
plt.title('Pronóstico de Ventas Futuras de Videojuegos basado en la Puntuación de los Críticos')
plt.legend()
plt.show()
