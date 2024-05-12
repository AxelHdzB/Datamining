import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Leer el archivo CSV de ventas de videojuegos
df = pd.read_csv("vgchartz-2024.csv")

# Concatenar las palabras de una columna relevante (por ejemplo, 'title', 'genre', 'publisher', etc.)
text = ' '.join(df['title'].dropna().astype(str).values)

# Crear el WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Mostrar la imagen del WordCloud
plt.figure(figsize=(14, 12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
