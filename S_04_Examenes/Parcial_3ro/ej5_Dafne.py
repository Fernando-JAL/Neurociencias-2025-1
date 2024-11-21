# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que, para cada nodo, se
# mantenga aquel nodo con mayor comunicación, con el nuevo arreglo muestre los nodos y vértices del grafo

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

# Cargar los datos
mat_path = r'C:\Users\daphn\Documents\UNAM\Neurociencias\Quinto semestre 1\Modelos\Git\Neurociencias-2025-1\BCT\BCT\2019_03_03_BCT\data_and_demos\Coactivation_matrix.mat'
mat_data = scipy.io.loadmat(mat_path)

# Obtener la matriz de coactivación
coactivation_matrix = mat_data['Coactivation_matrix']

# Filtrar para mantener solo la conexión de mayor peso por fila (nodo)
filtered_matrix = np.zeros_like(coactivation_matrix)
for i, row in enumerate(coactivation_matrix):
    max_index = np.argmax(row)  # Índice del mayor valor en la fila
    filtered_matrix[i, max_index] = row[max_index]  # Conservar la conexión más fuerte

# Verificar si hay coordenadas disponibles
if 'Coord' in mat_data:
    coords = mat_data['Coord']  # Coordenadas de los nodos

    # Separar las coordenadas
    x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]

    # Crear el grafo desde la matriz filtrada
    G = nx.from_numpy_array(filtered_matrix, create_using=nx.DiGraph)

    # Usar las coordenadas como posiciones de los nodos
    pos = {i: (x[i], y[i], z[i]) for i in range(len(x))}

    # Configurar la figura para graficar en 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Dibujar nodos
    ax.scatter3D(x, y, z, c='r', marker='o', s=50, label='Nodos')

    # Dibujar aristas
    for edge in G.edges():
        node1, node2 = edge
        ax.plot(
            [pos[node1][0], pos[node2][0]],
            [pos[node1][1], pos[node2][1]],
            [pos[node1][2], pos[node2][2]],
            color='b', alpha=0.7, label='Aristas' if edge == list(G.edges())[0] else ""  # Etiqueta una vez
        )

    # Configurar etiquetas y mostrar
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Grafo 3D con Mayor Comunicación por Nodo')
    ax.legend()
    plt.show()

else:
    print("No se encontraron coordenadas en el archivo .mat.")
