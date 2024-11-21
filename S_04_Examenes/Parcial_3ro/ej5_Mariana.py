# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que,
# para cada nodo, se mantenga aquel nodo con mayor comunicación,
# con el nuevo arreglo muestre los nodos y vértices del grafo.

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns


mat_path = "/Users/marianazuniga/Downloads/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_data = scipy.io.loadmat(mat_path)

c_m = mat_data['Coactivation_matrix']
n_nodes = c_m.shape[0]
filtrado = np.zeros_like(c_m)

for i in range(n_nodes):
    max_val = np.max(c_m[i])
    if max_val > 0:
        max_idx = np.argmax(c_m[i])
        filtrado[i, max_idx] = max_val


plt.figure(figsize=(10, 8))
sns.heatmap(filtrado, cmap='jet')
plt.title('Matriz Filtrada (Solo la Conexión Más Fuerte de Cada Nodo)')
plt.show()


coords = mat_data['Coord']

x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

G = nx.from_numpy_array(filtrado)
ax.scatter3D(x, y, z, c='r', marker='o', s=50)


for edge in G.edges():
    node1, node2 = edge
    connection_strength = filtrado[node1, node2]
    if connection_strength > 0.2:
        ax.plot([x[node1], x[node2]],
                [y[node1], y[node2]],
                [z[node1], z[node2]],
                color='g', alpha=0.7)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título del gráfico
ax.set_title('Grafo 3D con Solo Conexiones Fuertes')

# Mostrar el gráfico
plt.show()
