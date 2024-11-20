import scipy.io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

                                             ### EJERCICIO 1 ###

# Parte 0: Preparando los archivos y datos
mat_path = r"C:\Users\dnlls\PycharmProjects\BrainToolbox\BCT\2019_03_03_BCT\data_and_demos\Coactivation_matrix.mat"
mat_json = scipy.io.loadmat(mat_path)

coactivation_matrix = mat_json['Coactivation_matrix']

matDict = {k:v for k, v in mat_json.items() if k[0] != '_'}
matDict.keys()

# E1 Parte 1: Dataframe con columnas e índices numerados desde 1
df = pd.DataFrame(coactivation_matrix, index=range(1, coactivation_matrix.shape[0] + 1),
                  columns=range(1, coactivation_matrix.shape[1] + 1))
print('Imprimiendo DataFrame con columnas e índices numerados desde 1:', df)

# E1 Parte 2: Heatmap de coactivation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(df, cmap='magma')
plt.title("Heatmap de Coactivation Matrix")
plt.show()

# E1 Parte 3: Subconjunto del dataframe de la fila 10 a la 30 y de la columna 10 a la 30
df_subset = df.loc[10:30, 10:30]

# E1 Parte 4: Mostrar el heatmap del subconjunto
plt.figure(figsize=(8, 6))
sns.heatmap(df_subset, cmap='magma')
plt.title("Heatmap del subconjunto (Filas 10-30, Columnas 10-30)")
plt.show()

# E1 Parte 5: Crear el grafo dirigido del subconjunto
G = nx.from_pandas_adjacency(df_subset, create_using=nx.DiGraph())

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=700, font_size=10, font_weight='bold', arrows=True, arrowstyle='-|>')
plt.title("Grafo dirigido del subconjunto (Filas 10-30, Columnas 10-30)")
plt.show()

# E1 Parte 6: Determinar el nodo con más conexiones en el nuevo dataset
max_connections_node = max(G.out_degree, key=lambda x: x[1])
print(f"El nodo con más conexiones en el subconjunto es: {max_connections_node[0]}, con {max_connections_node[1]} conexiones.")

# E1 Parte 7: Calcular los quantiles 0.25, 0.5 y 0.75 de la matriz de coactivación completa
cx =df.values.flatten()
print('Los cuantiles para el arreglo son:\n',pd.Series(cx).quantile([0.25,0.5,0.75]))

cx0= cx[cx!= 0]
quantiles = pd.Series(cx0).quantile([0.25, 0.5, 0.75])
print('cuantiles:\n', quantiles)

# E1 Parte 8: Mostrar el histograma de distribución de los valores de la matriz de coactivación
plt.figure(figsize=(10, 6))
plt.hist(quantiles, bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma de distribución de valores de la matriz de coactivación")
plt.xlabel("Valor de coactivación")
plt.ylabel("Frecuencia")
plt.show()

# E1 Parte 9: Binarizar la matriz de coactivación del subconjunto usando un threshold de 0
df_subset_binary = df_subset.map(lambda x: 1 if x > 0 else 0)
print("Parte 9. Matriz binarizada:\n", df_subset_binary)

plt.figure(figsize=(8, 6))
sns.heatmap(df_subset_binary, cmap='viridis', cbar=False)
plt.title("Heatmap del subconjunto binarizado")
plt.show()
