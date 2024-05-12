import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv("vgchartz-2024.csv")


#Imagen 1: Top 10 de juegos mas vendidos
top_selling_games = df.groupby('title')['total_sales'].sum().nlargest(10)

# Configurar el estilo de seaborn
sns.set(style="whitegrid")

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=top_selling_games.values, y=top_selling_games.index, palette='rocket')

# Etiquetar las barras con las ventas
ax.bar_label(ax.containers[0], label_type='edge', fontsize=10, color='black', 
              bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.5))

# Formatear el eje y como millones
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}M'))

# Personalizar etiquetas y título
plt.xlabel('Total Sales (Millions)')
plt.ylabel('Game Titles')
plt.title('Top 10 Selling Games')

# Rotar las etiquetas del eje y para mejorar la legibilidad
plt.yticks(rotation=0)

#guardar el gráfico pero no muestra bien los datos
#plt.savefig('Top_Selling_Games.png')

# Mostrar el grafico ademas que puedes modificar y guardar la imagen a su conveniencia Top_Selling_Games
plt.show()



# Imagen 2: Comparacion de ventas entre diferentes distribuidoras
sorted_publishers = (
    df.groupby('publisher')['total_sales']
    .sum()
    .nlargest(150)
    .reset_index(name='total_sales')
)

# Configuraciones de estilo de seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 20))

# Crear el gráfico de puntos para las ventas totales por editor
ax = sns.scatterplot(x='total_sales', y='publisher', data=sorted_publishers, palette='muted', s=100, edgecolor='w')

# Configuraciones adicionales para el gráfico
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}M'))
plt.xlabel('Total Sales (Millions)')
plt.ylabel('Publisher')
plt.title('Total Sales by Publisher')

# Ajustar diseño y despues guardarlo como Total_Sales_by_Publisher
plt.show()



#Imagen 3: Géneros con mayor puntuación crítica
genre_stats=df.groupby('genre').agg({
    'critic_score':'median',
    'total_sales':'sum'
})
sorted_genres_by_score=genre_stats.sort_values(by='critic_score',ascending=False)
sorted_genres_by_sales=genre_stats.sort_values(by='total_sales',ascending=False)

palette = sns.color_palette("tab20", len(sorted_genres_by_score))

plt.figure(figsize=(10, 6))
ax=sns.barplot(x=sorted_genres_by_score.index, y=sorted_genres_by_score['critic_score'], palette=palette)
ax.bar_label(ax.containers[0], label_type='edge', fontsize=10, color='black', 
              bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.5))
plt.title('Genres with Highest Critic Scores')
plt.xlabel('Genre')
plt.ylabel('Median Critic Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

#Guardalo como Genres_Highest_Critic_Scores
plt.show()


plt.figure(figsize=(12, 6))
ax=sns.barplot(x=sorted_genres_by_sales.index, y=sorted_genres_by_sales['total_sales'], palette=palette)
ax.bar_label(ax.containers[0], label_type='edge', fontsize=10, color='black', 
              bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.5))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}M'))
plt.title('Genres with Highest Total Sales')
plt.xlabel('Genre')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



#Imagen #4:Juegos más vendidos por plataforma
platforms = df.groupby(['title', 'console'])['total_sales'].sum().sort_values(ascending=False).head(10)
titles = [index[0] for index in platforms.index]
consoles = [index[1] for index in platforms.index]
sales = platforms.values
unique_consoles = np.unique(consoles)
colors = plt.cm.tab20(np.linspace(0, 1, len(unique_consoles)))
console_colors = dict(zip(unique_consoles, colors))


sales_in_millions = sales  


plt.figure(figsize=(14, 10))
for i in range(len(titles)):
    console = consoles[i]
    color = console_colors[console]
    plt.bar(titles[i], sales_in_millions[i], color=color, label=console)

plt.xlabel('Game Titles')
plt.ylabel('Sales (Millions)')
plt.title('Top Selling Games by Platform')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Console',loc='best')


plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}M'))

plt.tight_layout()
#Guardalo como Top_Platform_Selling_Games:
plt.show()