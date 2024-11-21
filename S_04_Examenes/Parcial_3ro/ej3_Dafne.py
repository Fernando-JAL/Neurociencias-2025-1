import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.io

# Se carga el grado
G = nx.dodecahedral_graph()
# Se definen las coordenadas de cada nodo
mat_path = r"/BCT/BCT/2019_03_03_BCT/data_and_demos/fve30.mat"
mat_dict = scipy.io.loadmat(mat_path)

# Se usa la información de 'fve30.mat' para el grafo
G = nx.from_numpy_array(mat_dict['CIJ'])

# Se definen las coordenadas de cada nodo
x = np.random.randint(0, 51, size = 30)
y = np.random.randint(0, 51, size = 30)
z = np.random.randint(0, 51, size = 30)

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