## Examen 3er parcial: dataframes y grafos
#Alumna: Zaira Valentina Ávila Lazcano
# Ejercicio 5:
#Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que, para cada nodo, se mantenga aquel nodo con mayor comunicación, con el nuevo arreglo muestre los nodos y vértices del grafo

#*quedarnos con el nodo que tenga mayor conexion*


import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

ruta_archivo = "/Users/ZvalEnes/Desktop/Neurociencias-2025-1/BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
datos = scipy.io.loadmat(ruta_archivo)

coactivacion = datos['Coactivation_matrix']
num_nodos = coactivacion.shape[0]
matriz_filtrada = np.zeros_like(coactivacion)

for nodo in range(num_nodos):
    maximo = np.max(coactivacion[nodo])
    if maximo > 0:
        indice_max = np.argmax(coactivacion[nodo])
        matriz_filtrada[nodo, indice_max] = maximo

plt.figure(figsize=(10, 8))
sns.heatmap(matriz_filtrada, cmap='gray')
plt.title('Matriz Filtrada - Conexión Más Fuerte')
plt.show()

coordenadas = datos['Coord']

coord_x, coord_y, coord_z = coordenadas[:, 0], coordenadas[:, 1], coordenadas[:, 2]
grafica = plt.figure(figsize=(10, 7))
eje = grafica.add_subplot(111, projection="3d")

grafo_nx = nx.from_numpy_array(matriz_filtrada)
eje.scatter3D(coord_x, coord_y, coord_z, c='skyblue', marker='o', s=50)

for edge in grafo_nx.edges():
    nodo_a, nodo_b = edge
    fuerza_enlace = matriz_filtrada[nodo_a, nodo_b]
    if fuerza_enlace > 0.2:
        eje.plot([coord_x[nodo_a], coord_x[nodo_b]],[coord_y[nodo_a], coord_y[nodo_b]],[coord_z[nodo_a], coord_z[nodo_b]], color='red', alpha=0.7)

eje.set_title('Visualización 3D-Conexiones Fuertes')
eje.set_xlabel('Coordenada X')
eje.set_ylabel('Coordenada Y')
eje.set_zlabel('Coordenada Z')

plt.show()
