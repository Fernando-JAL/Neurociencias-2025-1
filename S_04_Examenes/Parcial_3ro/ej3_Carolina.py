import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.io import loadmat

# EJERCICIO 3: Modifique el código de animation2_2 para usar la información de 'fve30.mat'.
# Para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intevalor [0, 50].


data = loadmat(r'C:\Users\dnlls\PycharmProjects\EXAMEN3MODELOS\fve32.mat')

adj_matrix = data['CIJ']
G = nx.from_numpy_array(adj_matrix)

num_nodes = G.number_of_nodes()
x = np.random.randint(0, 50, size=num_nodes)
y = np.random.randint(0, 50, size=num_nodes)
z = np.random.randint(0, 50, size=num_nodes)

nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")

def init():
    ax.scatter(*nodes.T)
    for edge in edges:
        ax.plot(*edge.T)
    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i * 4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()
