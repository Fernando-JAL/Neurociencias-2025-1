# EJERCICIO 1.
# En un solo lanzamiento de dos dados de 6 caras (con el mismo peso), encuentre la probabilidad
# de que su suma sea como máximo 'n'. Cree una funcion llamada 'lanzamiento' que reciba un entero
# llamado 'n' y retorne un flotante que calcule la probabilidad de que el lanzamiento de 2 dados de
# 6 caras sea <= n.

n = 13 #Definimos valor de 'n'.
def lanzamiento(n: int) -> float: #Creamos la función
    total_combinaciones = 36
    combinaciones_validas = 0
    for dado1 in range(1, 7): #primer dado
        for dado2 in range(1, 7):  #segundo dado
            suma = dado1 + dado2
            if suma <= n: #condición para ver si la suma es <= n
                combinaciones_validas += 1
    #para calcular la probabilidad
    probabilidad = combinaciones_validas / total_combinaciones
    return probabilidad
print(f"La probabilidad de que la suma sea <= {n} es {lanzamiento(n)}")

#_______________________________________________________________________________________________________

# EJERCICIO 2.
# Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:

# ¿Qué forma tiene el grafo?
    # El grafo es un dodecaedro, una figura de doce caras, cada una de ellas con forma de pentagono.

# ¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
    # El grafo tiene 20 nodos, para llegar a este resultado se escribio el siguiente código:

            # print(G.number_of_nodes())

# ¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de aristas?
    # El grafo tiene 30 aristas, para llegar a este resultado se escribio el siguiente código:

            # print(G.number_of_edges())

# ¿Qué hace el código G.degree()?
    # Nos dice el grado de un nodo, y el grado se refiere al número de aristas incidentes a él. En este caso al
    # ser un grafo no direccionado solo nos arroja un valor, si fuera dirigido podriamos hacer la distinción
    # entre las aristas que entran y las que salen, para este ejercicio escribimos lo siguiente:

            # print(G.degree()): Que nos arrojó el número del nodo y su grado.
            # [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),
            # (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 3)]

            # print(G.degree([0, 1, 2])): Que nos arrojo el nodo y grado unicamente de los que especificamos.
            # [(0, 3), (1, 3), (2, 3)]

# ¿Cuál es el número máximo de aristas en el grafo?
    # Para calcular el número máximo de aristas en el grafo podemos usar el siguiente código, que al
    # final nos dira que "El número máximo de aristas en el grafo es = 190".

numero_de_nodos = 20
N = numero_de_nodos
def aristas_max(N, directed=False):
    if directed:
        return N * (N - 1)
    else:
        return (N * (N - 1)) // 2
print(f'El número máximo de aristas en el grafo es = {aristas_max(N, directed=False)}')

# ¿Cuál es la diferencia entre animation2_1 y animation2_2?
    # La diferencia está en las ultimas lineas del código. Estas se utilizaron para agregar una
    # animación de giro que no se observa en la animation 2_1:

            #def init():
                #return fig,
            #def animate(i):
                #ax.view_init(elev=20, azim=i*4)
                #return fig,
            #ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)

#_______________________________________________________________________________________________________

# EJERCICIO 3.
# Modifique el código de animation2_2 para usar la información de 'fve30.mat'. Para las coordenadas
# 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intervalo [0, 50].

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import scipy.io
from matplotlib import animation

file = scipy.io.loadmat(r"/home/bubbleth/PycharmProjects/pythonProject/Repo_Beth/fve30.mat")
G = nx.from_numpy_array(file['CIJ'])

# Se definen las coordenadas de cada nodo
x = np.random.randint(0, 51, size= 32)
y = np.random.randint(0, 51, size= 32)
z = np.random.randint(0, 51, size= 32)

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

#_______________________________________________________________________________________________________

# Ejercicio 4.
# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener los valores > 0.2,
# con el nuevo arreglo muestre los nodos y vértices del grafo.

import networkx as nx
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

datos = loadmat(r"/home/bubbleth/PycharmProjects/pythonProject/Repo_Beth/Coactivation_matrix.mat")

matrizx = np.array(datos['Coactivation_matrix'])
print(type(matrizx))
print(matrizx.size)
print(matrizx.ndim)
#print(matrizx)

matrizx1 = nx.from_numpy_array(datos['Coactivation_matrix'])
print(type(matrizx1))
print(matrizx1)

# #Ahora para filtrar la matriz usaremos
filtro_matrizx= matrizx[matrizx > 0.2]
print(type(filtro_matrizx))
print(filtro_matrizx.size)
print(filtro_matrizx.ndim)
#print(filtro_matrizx)

# Convertir los datos a un array
filtro_array= np.array(filtro_matrizx)

# Crear un grafo a partir del array filtrado
num_nodes = 12  # Número de nodos del grafo
weights = filtro_array.reshape((num_nodes, -1))  # Reshape para asociar pesos entre nodos

# Crear el grafo
graph = nx.Graph()
graph.add_nodes_from(range(num_nodes))  # Agregar nodos

# Agregar vértices con pesos al grafo
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        weight = weights[i, j % weights.shape[1]]  # Usar peso del array
        graph.add_edge(i, j, weight=weight)

# # Mostrar nodos y vértices
print("Nodos del grafo:")
print(graph.nodes())
print("\nVértices del grafo (con pesos):")
for edge in graph.edges(data=True):
    print(edge)

# Dibujar el grafo
pos = nx.spring_layout(graph)  # Posiciones para el dibujo
nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels={k: f"{v:.2f}" for k, v in labels.items()})
plt.title("Grafo generado a partir de datos filtrados")
plt.show()

#_______________________________________________________________________________________________________

# Ejercicio 5.
# Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que, para cada nodo, se
# mantenga aquel nodo con mayor comunicación, con el nuevo arreglo muestre los nodos y vértices
# del grafo.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm  # Import colormap
import networkx as nx
import scipy.io
from mpl_toolkits.mplot3d import Axes3D

#Subimos nuestros archivos
database1 = r"Coactivation_matrix.mat"
mat_rix = scipy.io.loadmat(database1)

#Cambiamos a diccionario
dictionary = {k: v for k, v in mat_rix.items() if k[0] != '_'}
df = pd.DataFrame(dictionary['Coactivation_matrix'])

G = nx.from_pandas_adjacency(df, create_using=nx.DiGraph)

#Aqui dejamos al nodo con uno de sus nodos mas conectado
for node in G.nodes():
    edges = G[node]
    if edges:
        VecMax = max(edges.items(), key=lambda x: x[1]['weight'])[0]
        for vecinos in list(edges.keys()):
            if vecinos != VecMax:
                G.remove_edge(node, vecinos)

nx.draw(G, node_color='blue', edge_color='pink', node_size=50)

#A numpy array
df_adj = nx.to_pandas_adjacency(G)
adj_matrix = df_adj.to_numpy()

#Definimos x, y, x
x = dictionary['Coord'][:, 0]
y = dictionary['Coord'][:, 1]
z = dictionary['Coord'][:, 2]

pesoMaximo = np.max(adj_matrix) if np.max(adj_matrix) > 0 else 1  #Evita división sobre '
pesosNormalizados = adj_matrix / pesoMaximo  #Pesos sólo del 0 al 1
colormap = cm.viridis #Colormap

#Figura
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(x, y, z, color='green', s=50)

#Plot edges
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix)):
        weight = adj_matrix[i, j]
        if weight > 0:  #Sólo non zero edges
            color = colormap(pesosNormalizados[i, j])  #Color of edges according to weight
            ax.plot(
                [x[i], x[j]],
                [y[i], y[j]],
                [z[i], z[j]],
                color=color, alpha=0.8, lw=1 + 3 * weight  #Brighter
            )

ax.view_init(elev=20., azim=30)

plt.show()
