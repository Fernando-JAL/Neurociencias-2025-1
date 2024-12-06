import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import animation2_1
import animation2_2


# EJERCICIO 2: Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:

# 1. ¿Qué forma tiene el grafo?
    # animation2_1: forma de dodecaedro
    # animation2_2: forma de dodecaedro

# 2. ¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
    # Los grafos de ambos archivos tienen 20 nodos o vértices.
    # Se puede descubrir el número de nodos con el comando:
        # num_vertices = G.number_of_nodes()

print('animation2_1 número de nodos:', animation2_1.G.number_of_nodes())
print('animation2_2 número de nodos:', animation2_2.G.number_of_nodes())

# 3. ¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de aristas?
    # Los grafos de ambos archivos tienen 30 aristas.
    # Se puede descubrir el número de aristas con el comando:
        # num_edges = G.number_of_edges()

print('\n animation2_1 número de aristas:', animation2_1.G.number_of_edges())
print('animation2_2 número de aristas:', animation2_2.G.number_of_edges())

# 4. ¿Qué hace el código G.degree()?
    # G.degree() se utiliza para calcular el grado de cada nodo de un grafo G

# 5. ¿Cuál es el número máximo de aristas en el grafo?
    # Los grafos de ambos archivos tienen un número máximo de aristas de 190.

n = animation2_1.G.number_of_nodes()
max_aristas = n * (n - 1) // 2
print("\n Número máximo de aristas animation2_1:", max_aristas)

z = animation2_2.G.number_of_nodes()
max_aristas = z * (z - 1) // 2
print("Número máximo de aristas animation2_2:", max_aristas)


# ¿Cuál es la diferencia entre animation2_1 y animation2_2?
    # Ambos códigos crean un grafo en 3D de un dodecaedro. Sus diferencias radican en que animation2_1 genera
    # una representación estática del grafo y hace un análisis de los datos porque calcula el grado de los
    # nodos con G.degree() y grafica un histograma de distribución.
    #
    # Por otro lado, animation2_2 utiliza 'FuncAnimation' para crear una animación en la que la
    # vista del grafo gira automáticamente, pero no incluye análisis del grafo.


