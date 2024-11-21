## Examen 3er parcial: dataframes y grafos
#Alumna: Zaira Valentina Ávila Lazcano

# Ejercicio 4:
#Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener los valores > 0.2, con el nuevo arreglo muestre los nodos y vértices del grafo

#*practicar filtrados, nodos con mayor conexion*


import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

ruta_matriz = "/Users/ZvalEnes/Desktop/Neurociencias-2025-1/BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
datos_matriz = scipy.io.loadmat(ruta_matriz)

matriz_coact = datos_matriz['Coactivation_matrix']
filtrada = np.where(matriz_coact > 0.2, matriz_coact, 0)

if 'Coord' in datos_matriz:
    coord = datos_matriz['Coord']
    coord_x, coord_y, coord_z = coord[:, 0], coord[:, 1], coord[:, 2]

# grafo 3D
figura = plt.figure(figsize=(10, 7))
eje = figura.add_subplot(111, projection="3d")

grafo = nx.from_numpy_array(filtrada)

# nodos
eje.scatter3D(coord_x, coord_y, coord_z, c='skyblue', marker='o', s=60)

#  conexiones del grafo
for arista in grafo.edges():
    nodo_a, nodo_b = arista
    eje.plot([coord_x[nodo_a], coord_x[nodo_b]], [coord_y[nodo_a], coord_y[nodo_b]], [coord_z[nodo_a], coord_z[nodo_b]], color='red', alpha=0.6)


eje.set_title('Grafo 3D-Conexiones Filtradas')
eje.set_xlabel('Coordenada X')
eje.set_ylabel('Coordenada Y')
eje.set_zlabel('Coordenada Z')

plt.show()
