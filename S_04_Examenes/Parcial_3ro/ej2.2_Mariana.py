import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

# Se carga el grafo del dodecaedro
G = nx.dodecahedral_graph()

# Coordenadas de los nodos
x = np.array([-1.0, -0.74535599, -0.33333333, -0.33333333, 0.33333333,
              0.74535599, 0.33333333, 0.33333333, -0.33333333, -0.33333333,
              -0.74535599, -0.33333333, 0.33333333, 0.33333333, 0.74535599,
              1.0, 0.74535599, 0.33333333, -0.33333333, -0.74535599])

y = np.array([-0.13278077, 0.5418651, 0.81169596, 0.30381473, 0.14755841,
              0.55886793, 0.96932751, 0.79691831, 0.53273201, -0.14755841,
              -0.55886793, -0.96932751, -0.81169596, -0.30381473, 0.27990399,
              0.13278077, -0.5418651, -0.53273201, -0.79691831, -0.27990399])

z = np.array([-0.0675157, 0.11842486, -0.39102575, -0.89182412, -0.91126968,
              -0.42248934, -0.10096091, 0.58775964, 0.7233475, 0.91126968,
              0.42248934, 0.10096091, 0.39102575, 0.89182412, 0.69188391,
              0.0675157, -0.11842486, -0.7233475, -0.58775964, -0.69188391])

# Coordenadas de los nodos
nodes = np.array([[i, j, k] for i, j, k in zip(x, y, z)])

# Crear figura y ejes 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

def init():
    ax.clear()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

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


#¿Cuál es la diferencia entre animation2_1 y animation2_2?
#La diferencia netre los dos cógigos es que en el animation 2 se genera una animación en 3D
#usando from matplotlib import animation, doonde la animación rota. Así mismo en animation 1
# cambia el estilo visual, se colorean de diferentes colores los 30 aristas y se muestra un
# historgrama con el número de aristas conectadas a cada nodo.
