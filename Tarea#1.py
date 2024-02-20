# Dataset sacado de: https://www.kaggle.com/datasets/asaniczka/video-game-sales-2024/data

import pandas as pd

#Leera el archivo csv si este mismo se encuentra en la misma carpeta donde esta este script
data = pd.read_csv("vgchartz-2024.csv")

# Elimina columna img
data = data.drop('img', axis=1)

# Elimina columna release_date
data = data.drop('release_date', axis=1)

# Elimina columna last_update
data = data.drop('last_update', axis=1)

print(data)

# Guarda el nuevo csv con los datos limpios
data.to_csv('New_vgchartz-2024.csv', index=True)