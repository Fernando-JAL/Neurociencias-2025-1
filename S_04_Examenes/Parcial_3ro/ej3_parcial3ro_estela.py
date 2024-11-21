import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io
from matplotlib import animation

mat_path = scipy.io.loadmat(r"C:\Users\estel\OneDrive\Escritorio\NEUROCIENCIAS\QUINTO SEMESTRE\MODELOS\Neurociencias-2025-1\BCT\BCT\2019_03_03_BCT\data_and_demos\fve30.mat")
G = nx.from_numpy_array(mat_path['CIJ'])
# modifica el código de animation2_2 para usar la información de 'fve30.mat'
# para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intrevalo [0, 50]

x = np.random.randint(0, 51, size  = 32)
y = np.random.randint(0, 51, size = 32)
z = np.random.randint(0, 51, size = 32)

nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(111, projection="3d")


def init():
    ax.scatter(*nodes.T, c='b', marker='o')  # nodos
    for edge in edges:
        ax.plot(*edge.T, c='k')  # aristas

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_zlim(0, 50)

    return fig,


def animacion(i):
    ax.view_init(elev=20, azim=i * 4)
    return fig,

animation = animation.FuncAnimation(fig, animacion, init_func=init, frames=90, interval=200, blit=False)
plt.show()
