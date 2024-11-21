# Modifique el código de animation2_2 para usar la información de 'fve30.mat'.
# Para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intevalor [0, 50]

import scipy.io
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

mat_path = "/Users/marianazuniga/Downloads/BCT/2019_03_03_BCT/data_and_demos/fve30.mat"
mat_data = scipy.io.loadmat(mat_path)
cij = mat_data['CIJ']

# Crear el grafo desde la matriz de adyacencia
G = nx.from_numpy_array(cij)

# Generar coordenadas aleatorias en el intervalo [0, 50]
num_nodes = G.number_of_nodes()
x = np.random.randint(0, 51, size=num_nodes)
y = np.random.randint(0, 51, size=num_nodes)
z = np.random.randint(0, 51, size=num_nodes)

# Coordenadas combinadas para cada nodo
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])

# Crear figura y ejes 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

def init():
    ax.clear()
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])
    ax.set_zlim([0, 50])

    # Dibujar nodos
    ax.scatter(x, y, z, color="blue", s=50)

    # Dibujar aristas
    for u, v in G.edges():
        x_edge = [nodes[u][0], nodes[v][0]]
        y_edge = [nodes[u][1], nodes[v][1]]
        z_edge = [nodes[u][2], nodes[v][2]]
        ax.plot(x_edge, y_edge, z_edge, color="black")

    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i * 4)  # Rotar la vista
    return fig,

# Crear la animación
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

# Mostrar el gráfico
plt.show()


mat_path = "/Users/marianazuniga/Downloads/BCT/2019_03_03_BCT/data_and_demos/fve30.mat"
mat_data = scipy.io.loadmat(mat_path)
cij = mat_data['CIJ']

# Crear el grafo desde la matriz de adyacencia
G = nx.from_numpy_array(cij)

# Generar coordenadas aleatorias en el intervalo [0, 50]
num_nodes = G.number_of_nodes()
x = np.random.randint(0, 51, size=num_nodes)
y = np.random.randint(0, 51, size=num_nodes)
z = np.random.randint(0, 51, size=num_nodes)

# Coordenadas combinadas para cada nodo
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])

# Crear figura y ejes 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

def init():
    ax.clear()
    ax.set_xlim([0, 50])
    ax.set_ylim([0, 50])
    ax.set_zlim([0, 50])

    # Dibujar nodos
    ax.scatter(x, y, z, color="blue", s=50)

    # Dibujar aristas
    for u, v in G.edges():
        x_edge = [nodes[u][0], nodes[v][0]]
        y_edge = [nodes[u][1], nodes[v][1]]
        z_edge = [nodes[u][2], nodes[v][2]]
        ax.plot(x_edge, y_edge, z_edge, color="black")

    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i * 4)  # Rotar la vista
    return fig,

# Crear la animación
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

# Mostrar el gráfico
plt.show()

