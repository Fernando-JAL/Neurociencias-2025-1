
# Modifique el código de animation2_2 para usar la información de 'fve30.mat'. Para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intevalor [0, 50]
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io
from matplotlib import animation

# Se carga el archivo
file_path = '/Users/sabrina/Documents/UNI/A-NEUROCIENCIAS/QUINTO /MODELOS/Neurociencias-2025-1/BCT/BCT/2019_03_03_BCT/data_and_demos/fve30.mat'  # Cambia esta ruta si es necesario
data = scipy.io.loadmat(file_path)  # Cargar el archivo
adj_matrix = data['CIJ']

# crear grafo
G = nx.from_numpy_array(adj_matrix)

# coordenadas aleatorias del 0 al 50
num_nodes = len(G.nodes)
x = np.random.randint(0, 50, num_nodes)
y = np.random.randint(0, 50, num_nodes)
z = np.random.randint(0, 50, num_nodes)


# Se crean los nodos y las aristas acorde al grafo
nodes = np.array([[x[i], y[i], z[i]] for i in range(num_nodes)])
edges = [(nodes[u], nodes[v]) for u, v in G.edges()]

# Se grafica
fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection="3d")

def init():
    ax.scatter(nodes[:, 0], nodes[:, 1], nodes[:, 2], color='blue', s=50)
    for edge in edges:
        ax.plot(*zip(edge[0], edge[1]), color='gray')
    return fig,

# para animarla
def animate(i):
    ax.view_init(20, i * 4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()


