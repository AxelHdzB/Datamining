import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Cargar el archivo CSV
df = pd.read_csv("vgchartz-2024.csv")

# Definir el número de los principales editores a considerar
top_publishers_count = 7  

# Agrupar los datos por 'Publisher' y calcular las ventas globales totales para cada editor
publisher_global_sales = df.groupby('publisher')['total_sales'].sum().nlargest(top_publishers_count)

# Filtrar los datos para los principales editores
data_top_publishers = df[df['publisher'].isin(publisher_global_sales.index)]

# Crear un gráfico de caja mostrando la distribución de las ventas globales para los principales editores
plt.figure(figsize=(10, 6))
sns.boxplot(x='publisher', y='total_sales', data=data_top_publishers)
plt.xlabel('Editor')
plt.ylabel('Ventas Totales')
plt.title(f'Distribución de Ventas Globales para los Top {top_publishers_count} Editores')
plt.xticks(rotation=45)
plt.grid(True)

# Realizar una prueba ANOVA de una vía para determinar si existen diferencias significativas en las ventas globales entre los editores
publisher_groups = [data_top_publishers[data_top_publishers['publisher'] == publisher]['total_sales'] for publisher in publisher_global_sales.index]
data_top_publishers = data_top_publishers.dropna()
for publisher, sales in zip(publisher_global_sales.index, publisher_groups):
    print(f"Editor: {publisher}")
    print(sales)
    print()


publisher_groups = [data_top_publishers[data_top_publishers['publisher'] == publisher]['total_sales'] for publisher in publisher_global_sales.index]
f_statistic, p_value = f_oneway(*publisher_groups)

# Imprimir resultados
print(f'Estadística F del ANOVA de una vía: {f_statistic:.2f}')
print(f'Valor p: {p_value:.4f}')

# Interpretar los resultados
alpha = 0.05  
if p_value < alpha:
    print("Existen diferencias significativas en las ventas globales entre los principales editores.")
    # Realizar la prueba de Tukey
    tukey_results = pairwise_tukeyhsd(data_top_publishers['total_sales'], data_top_publishers['publisher'])
    # Mostrar los resultados de la prueba de Tukey
    print(tukey_results)

else:
    print("No existen diferencias significativas en las ventas globales entre los principales editores.")
