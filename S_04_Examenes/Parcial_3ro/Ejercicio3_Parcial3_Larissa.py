### Ejercicio 3!!
# Modifique el código de animation2_2 para usar la información de 'fve30.mat'. Para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intevalor [0, 50]

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import scipy.io


data_path = scipy.io.loadmat(r"C:\Users\laris\OneDrive\Documentos\Modeloscomputacionales\Modelos-de-Larissa\fve30.mat")

G = nx.from_numpy_array(data_path['CIJ'])

num_nodes = G.number_of_nodes()
x = np.random.randint(0, 51, size=num_nodes)
y = np.random.randint(0, 51, size=num_nodes)
z = np.random.randint(0, 51, size=num_nodes)

# Nodos y las aristas en base a las coordenadas
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

# Configuración de la figura
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

# Función para inicializar la animación
def init():
    ax.scatter(*nodes.T, color="green", s=80)  # Nodos en verde
    for edge in edges:
        ax.plot(*edge.T, color="gray", alpha=0.6)  # Aristas en gris
    return fig,


def animate(i):
    ax.view_init(elev=20, azim=i * 4)  # Rotar sobre el eje azimutal
    return fig,

# Crear la animación
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.show()
