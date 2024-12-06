# Ejercicio 2

# Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib as mpl

# Se carga el grado del dodecaedro
G = nx.dodecahedral_graph()
# Se definen las coordenadas de cada nodo
x = np.array([-1.        , -0.74535599, -0.33333333, -0.33333333,  0.33333333, 0.74535599,  0.33333333,  0.33333333, -0.33333333, -0.33333333, -0.74535599, -0.33333333,  0.33333333,  0.33333333,  0.74535599, 1.        ,  0.74535599,  0.33333333, -0.33333333, -0.74535599])
y = np.array([-0.13278077,  0.5418651 ,  0.81169596,  0.30381473,  0.14755841, 0.55886793,  0.96932751,  0.79691831,  0.53273201, -0.14755841, -0.55886793, -0.96932751, -0.81169596, -0.30381473,  0.27990399, 0.13278077, -0.5418651 , -0.53273201, -0.79691831, -0.27990399])
z = np.array([-0.0675157 ,  0.11842486, -0.39102575, -0.89182412, -0.91126968, -0.42248934, -0.10096091,  0.58775964,  0.7233475 ,  0.91126968, 0.42248934,  0.10096091,  0.39102575,  0.89182412,  0.69188391, 0.0675157 , -0.11842486, -0.7233475 , -0.58775964, -0.69188391])

# Se crean los nodos y las aristas acorde al grafo
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])
edges = np.array([(nodes[u], nodes[v]) for u, v in G.edges()])

random_sizes = np.random.randint(50, 500, size=len(nodes))


# Se grafica
fig = plt.figure(figsize = (15, 15))
ax = fig.add_subplot(111, projection="3d")

# Se grafican los nodos
ax.scatter(*nodes.T)  # Equivalente a ax.scatter(x, y, z)
# Se grafican las aristas
for edge in edges:
    ax.plot(*edge.T)

plt.show()

# Calcula el grado de cada nodo y lo convierte a un diccionario
degrees = dict(G.degree())

# Grafica el histograma
plt.hist(degrees.values())
plt.show()

#¿Qué forma tiene el grafo?
#Un dodecaedro, donde cada cara es un pentágono regular.

#¿Cuántos nodos tiene el grafo?
#El grafo tiene 20 nodos

#¿con qué comando descubres el número de nodos?
G.number_of_nodes()

#¿Cuántas aristas tiene el grafo?
#el grafo tiene 30 aristas

#¿con qué comando descubres el número de aristas?
G.number_of_edges()

#¿Qué hace el código G.degree()?
# Devuelve el grado de cada nodo en el gráfico G.
# El grado es el número de aristas conectadas a cada nodo.

#¿Cuál es el número máximo de aristas en el grafo?
import networkx as nx
G = nx.dodecahedral_graph()
n = G.number_of_nodes()
max_aristas = n * (n - 1) // 2

print(f"El número máximo de aristas para un grafo con {n} nodos es: {max_aristas}")

