# EJERCICIO 4:
'''Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener los valores > 0.2,
con el nuevo arreglo muestre los nodos y vértices del grafo.'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import networkx as nx
from matplotlib.animation import FuncAnimation

archivo = scipy.io.loadmat(r"C:\Users\vladi\OneDrive\Documentos\PYTHON\Coactivation_matrix.mat")

dict = {k: v for k, v in archivo.items() if k[0] != '_'}
matriz = dict['Coactivation_matrix']
coord = dict['Coord']

fil_mat = np.where(matriz > 0.2, matriz, 0)
G = nx.from_numpy_array(fil_mat)

x, y, z = coord[:, 0], coord[:, 1], coord[:, 2]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

def init():
    ax.scatter(x, y, z, c='orange', s=50, label='Noditos ☻', marker='^')

    for edge in G.edges():
        node1, node2 = edge
        x_coords = [x[node1], x[node2]]
        y_coords = [y[node1], y[node2]]
        z_coords = [z[node1], z[node2]]
        ax.plot(x_coords, y_coords, z_coords, c='blue', alpha=0.5)


    ax.set_title("Grafo Chido de Coactivación Filtrado XD ☻")
    ax.set_xlabel('X (equis jsjs)')
    ax.set_ylabel('y (lle jsjs)')
    ax.set_zlabel('z (seta jsjs')
    ax.legend()
    return fig,

def animate(frame):
    ax.view_init(elev=20, azim=frame)
    return fig,

ani = FuncAnimation(fig, animate, init_func=init, frames=360, interval=50, blit=False)
plt.show()