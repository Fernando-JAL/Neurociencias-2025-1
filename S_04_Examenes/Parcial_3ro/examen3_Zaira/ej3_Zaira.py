## Examen 3er parcial: dataframes y grafos
#Alumna: Zaira Valentina Ávila Lazcano
# Ejercicio 3:
#Modifique el código de animation2_2 para usar la información de 'fve30.mat'. Para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intevalor [0, 50]
#*al pilotearlo se vera un cubo*

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.io import loadmat

# 'fve30.mat'
data = loadmat('/Users/ZvalEnes/Desktop/Neurociencias-2025-1/BCT/BCT/2019_03_03_BCT/data_and_demos/fve30.mat')
#  matriz de adyacencia (CIJ) y generar el grafo
CIJ = data['CIJ']
G = nx.from_numpy_array(CIJ)

#  coordenadas aleatorias en el intervalo [0, 50] para x, y, z
num_nodes = G.number_of_nodes()
np.random.seed(42)  # Fijar semilla para reproducibilidad
coordinates = np.random.randint(0, 51, size=(num_nodes, 3))


x, y, z = coordinates.T

#  nodos y aristas
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

fig = plt.figure(figsize=(10, 10))
eje = fig.add_subplot(111, projection="3d")

def init():
    eje.scatter(*nodes.T, color='red', s=50)  # Graficar nodos
    for edge in edges:  # Graficar aristas
        eje.plot(*edge.T, color='skyblue', alpha=0.7)
    eje.set_xlim(0, 50)
    eje.set_ylim(0, 50)
    eje.set_zlim(0, 50)
    return fig,

def animate(i):
    eje.view_init(elev=20, azim=i * 4)
    return fig,
eje.set_title('Visualización 3D')
eje.set_xlabel('Coordenada X')
eje.set_ylabel('Coordenada Y')
eje.set_zlabel('Coordenada Z')
# Animación
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()