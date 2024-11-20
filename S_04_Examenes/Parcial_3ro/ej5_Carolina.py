import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.io import loadmat

# EJERCICIO 5: Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que, para cada nodo,
# se mantenga aquel nodo con mayor comunicación, con el nuevo arreglo muestre los nodos y vértices del grafo

fileCM = loadmat(r"C:\Users\dnlls\PycharmProjects\EXAMEN3MODELOS\Coactivation_matrix.mat")
matx = fileCM.get('Coactivation_matrix', None)
coord = fileCM.get('Coord', None)

f_matx = np.zeros_like(matx)

f_matx = np.array([[1 if val == np.max(row) else 0 for val in row] for row in matx])

G = nx.from_numpy_array(f_matx)

x, y, z = coord[:, 0], coord[:, 1], coord[:, 2]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, s=10, marker='d', c='green')

for node1, node2 in G.edges():
    ax.plot([x[node1], x[node2]], [y[node1], y[node2]], [z[node1], z[node2]], c='#00aae4', alpha=0.5)

ax.set_title("Grafo Ejercicio 5")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
