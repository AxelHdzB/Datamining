import pandas as pd

# Leer el archivo CSV
data = pd.read_csv("vgchartz-2024.csv")

# Eliminar columnas 'img' y 'last_update'
data = data.drop(['img', 'last_update'], axis=1)

# Eliminar filas con valores nulos en las columnas de interés
data = data.dropna(subset=['developer', 'total_sales'])

# Agrupar por desarrollador y calcular las estadísticas descriptivas 
developer_stats = data.groupby('developer')['total_sales'].agg(['count', 'min', 'max', 'sum', 'mean', 'median'])

# Renombrar las columnas para mayor claridad
developer_stats.columns = ['count', 'min_total_sales', 'max_total_sales', 'total_sales_sum', 
                           'total_sales_mean', 'total_sales_median']

# Mostrar las estadísticas descriptivas por desarrollador
print(developer_stats)

# Guardar las estadísticas descriptivas en un archivo CSV
developer_stats.to_csv('developer_stats.csv', index=True)
