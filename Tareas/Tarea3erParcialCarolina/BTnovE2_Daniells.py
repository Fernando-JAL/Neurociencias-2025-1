import scipy.io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

                                             ### EJERCICIO 2 ###

# E2 Parte 0: Preparando archivos y datos
fvemat = scipy.io.loadmat(r"C:\Users\dnlls\PycharmProjects\BrainToolbox\BCT\2019_03_03_BCT\data_and_demos\fve32.mat")

# E2 Parte 1: Muestra el heatmap de la matriz de activación
fvemat_dict= {k:v for k, v in fvemat.items()if k[0] != '_'}
plt.figure(figsize=(15, 10))
sns.heatmap(fvemat_dict['CIJ'],cmap='YlGnBu',vmax= 2)
plt.title('Heatmap de fve32.mat')
plt.show()

# E2 Parte 2: Utilizando los nombres del archivo .mat, muestra el grafo en 4 formas distintas
# (shell debe ser una de ellas)

framedate = pd.DataFrame(fvemat_dict['CIJ'], index= fvemat_dict['Names'], columns= fvemat_dict['Names'])
G = nx.Graph(framedate)
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title('fve32.map en estándar')
nx.draw_networkx(G, node_color='y', with_labels=True)
plt.show()

plt.subplot(2, 2, 2)
plt.title('fve32.map en Circular')
nx.draw_circular(G, node_color='r', with_labels=True)
plt.show()

plt.subplot(2, 2, 3)
plt.title('fve32.map en Shell')
Pform = nx.shell_layout(G)
nx.draw(G, Pform, with_labels=True)
plt.show()

plt.subplot(2, 2, 4)
plt.title('fve32.map en Kamada-Kawai')
Pformkamada = nx.kamada_kawai_layout(G)
nx.draw(G, Pformkamada, with_labels=True, node_color= 'olivedrab')
plt.show()

# E2 Parte 3: Determina el nodo con mayores conexiones
maxnode = max(G.degree, key=lambda x: x[1])
print(f"El nodo con más conexiones es {maxnode[0]}")

# E2 Parte 4: Muestra el grado solo destacando las conexiones del nodo encontrado en el ejercicio anterior
print(f"El nodo del ejercicio anterior, tiene un grado de: {maxnode[1]/2}")