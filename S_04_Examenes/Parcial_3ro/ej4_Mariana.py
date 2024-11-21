#Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener los valores
# > 0.2, con el nuevo arreglo muestre los nodos y vértices del grafo


import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

mat_path = "/Users/marianazuniga/Downloads/BCT/2019_03_03_BCT/data_and_demos/Coactivation_matrix.mat"
mat_data = scipy.io.loadmat(mat_path)


c_m = mat_data['Coactivation_matrix']
filtrado = np.where(c_m > 0.2, c_m, 0)

mat_dict = mat_data
if 'Coord' in mat_dict:
    coords = mat_dict['Coord']

    x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    G = nx.from_numpy_array(filtrado)

    # Dibujar el grafo en 3D
    pos = {i: (x[i], y[i], z[i]) for i in range(len(x))}  # Usar las coordenadas para los nodos

    # Dibujar los nodos
    ax.scatter3D(x, y, z, c='r', marker='o', s=50)

    # Dibujar las conexiones (aristas) del grafo
    for edge in G.edges():
        node1, node2 = edge
        ax.plot([pos[node1][0], pos[node2][0]],
                [pos[node1][1], pos[node2][1]],
                [pos[node1][2], pos[node2][2]],
                color='b', alpha=0.7)

    # Etiquetas de los ejes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Título del gráfico
    ax.set_title('Grafo con matriz filtrada')

    # Mostrar el gráfico
    plt.show()

else:
    print("No se encontraron coordenadas en el archivo .mat.")