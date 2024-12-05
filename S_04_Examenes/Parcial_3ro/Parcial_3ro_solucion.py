import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io
from matplotlib import animation

#######################################################################################################################
# EJERCICIO 1
def lanzamiento(n):
    lados = [1, 2, 3, 4, 5, 6]
    lanzamientos = [[i, j] for i in lados for j in lados if i+j <= n]
    return len(lanzamientos)/len(lados)**2

suma = 9
print('Probabilidad es:', lanzamiento(suma))


#######################################################################################################################
# EJERCICIO 2

# - ¿Qué forma tiene el grafo?
# Tiene forma de dodecaedro

# - ¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
# 20 nodos, con len(G.nodes) = G.number_of_nodes()

# - ¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de nodos?
# 30 aristas, con len(G.edges) = G.number_of_edges()

# - ¿Qué hace el código G.degree()?
# Retorna el número de aristas adyacentes a cada nodo

# - ¿Cuál es el número máximo de aristas en el grafo?
# 3

# - ¿Cuál es la diferencia entre animation2_1 y animation2_2?
# animation2_2 muestra la animación del dodecaedro, animation2_1 muestra el plot


#######################################################################################################################
# EJERCICIO 3

# Leer datos
mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/fve30.mat"
mat_data = scipy.io.loadmat(mat_path)

# guardar los datos en variables propias
cij = mat_data['CIJ']
names = mat_data['Names']

# Se crea el grafo
G = nx.from_numpy_array(cij)
# Se definen las coordenadas de cada nodo
x, y, z = np.random.randint(0, 50, size=[3, len(cij)])

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


#######################################################################################################################
# EJERCICIO 4
import matplotlib.colors as colors
import matplotlib.cm as cmx

# Leer datos
mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_data = scipy.io.loadmat(mat_path)

# guardar los datos en variables propias
cij = mat_data['Coactivation_matrix']
coords = mat_data['Coord']

# Se crea el grafo
activation_dummy = cij > 0.2
G = nx.from_numpy_array(activation_dummy)

# Se crean los nodos y las aristas acorde al grafo
nodes = coords
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])
# variables para colores en aristas
color_values = [activation_dummy[u, v] for u, v in G.edges()]
jet = plt.get_cmap('jet')
cNorm = colors.Normalize(vmin=min(color_values), vmax=max(color_values))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

# Se grafica
fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection="3d")

def init():
    # Se grafican los nodos
    ax.scatter(*nodes.T)  # Equivalente a ax.scatter(x, y, z)
    # Se grafican las aristas
    for idx, vizedge in enumerate(edges):
        colorVal = scalarMap.to_rgba(color_values[idx])
        ax.plot(*vizedge.T, color=colorVal)

    return fig,

def animate(i):
    ax.view_init(elev=20, azim=i*4)
    return fig,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
plt.colorbar(scalarMap)
plt.show()


#######################################################################################################################
# EJERCICIO 5

# Leer datos
mat_path = r"../../BCT/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_data = scipy.io.loadmat(mat_path)

# guardar los datos en variables propias
cij = mat_data['Coactivation_matrix']
coords = mat_data['Coord']

# Se hace filtrado de matriz de adjacencia
activation_dummy = np.zeros(cij.shape)
for idx in range(len(cij)):
    maximum_idx_value_h = np.where(cij[idx, :] == max(cij[idx, :]))[0]
    maximum_idx_value_v = np.where(cij[:, idx] == max(cij[:, idx]))[0]
    activation_dummy[idx, maximum_idx_value_h] = cij[idx, maximum_idx_value_h]
    activation_dummy[maximum_idx_value_v, idx] = cij[maximum_idx_value_v, idx]

# Se crea el grafo
G = nx.from_numpy_array(activation_dummy)

# Se crean los nodos y las aristas acorde al grafo
nodes = coords
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])
# variables para colores en aristas
color_values = [activation_dummy[u, v] for u, v in G.edges()]
jet = plt.get_cmap('jet')
cNorm = colors.Normalize(vmin=min(color_values), vmax=max(color_values))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

# Se grafica
fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection="3d")

# Se grafican los nodos
ax.scatter(*nodes.T)  # Equivalente a ax.scatter(x, y, z)
# Se grafican las aristas
for idx, vizedge in enumerate(edges):
    colorVal = scalarMap.to_rgba(color_values[idx])
    ax.plot(*vizedge.T, color=colorVal)

plt.colorbar(scalarMap)
plt.show()
