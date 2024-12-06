"""Ejercicio 3
# Alisson García Mejía
# Modifique el código de animation2_2 para usar la información
 de 'fve30.mat'. Para las coordenadas 'x', 'y', 'z' utiliza un
 arreglo de números enteros aleatorios en el intevalor [0, 50]
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io
from matplotlib import animation

# Cargamos fv30
arch = scipy.io.loadmat(r"C:\Users\aliss\Downloads\fve30.mat")

G = nx.from_numpy_array(arch['CIJ'])

# Se definen las coordenadas de cada nodo
x = np.random.randint(0, 51, size= 32)
y = np.random.randint(0, 51, size= 32)
z = np.random.randint(0, 51, size= 32)

# Se crean los nodos y las aristas acorde al grafo
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

# Se grafica
fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection="3d")

def init():
    # Se grafican los nodos
    ax.scatter(*nodes.T)  # Equivalente a ax.scatter(x, y, z)
    # Se grafican las aristas
    for edge in edges:
        ax.plot(*edge.T)

    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()


