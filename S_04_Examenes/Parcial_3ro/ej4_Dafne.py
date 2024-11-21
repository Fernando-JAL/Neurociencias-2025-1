# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener
# los valores > 0.2, con el nuevo arreglo muestre los nodos y vértices del grafo

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

mat_path = r'C:\Users\daphn\Documents\UNAM\Neurociencias\Quinto semestre 1\Modelos\Git\Neurociencias-2025-1\BCT\BCT\2019_03_03_BCT\data_and_demos\Coactivation_matrix.mat'
mat_data = scipy.io.loadmat(mat_path)

coactivation_matrix = mat_data['Coactivation_matrix']

filtrado = np.where(coactivation_matrix > 0.2, coactivation_matrix, 0)

mat_dict = mat_data
if 'Coord' in mat_dict:
    coords = mat_dict['Coord']

    x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    G = nx.from_numpy_array(filtrado)

    # Grafo en 3D
    pos = {i: (x[i], y[i], z[i]) for i in range(len(x))}  # Usar las coordenadas para los nodos

    # Nodos
    ax.scatter3D(x, y, z, c='r', marker='o', s=50)

    # Aristas
    for edge in G.edges():
        node1, node2 = edge
        ax.plot([pos[node1][0], pos[node2][0]],
                [pos[node1][1], pos[node2][1]],
                [pos[node1][2], pos[node2][2]],
                color='b', alpha=0.7)


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Grafo 3D matriz filtrada')
    plt.show()

else:
    print("No se encontraron coordenadas en el archivo .mat.")