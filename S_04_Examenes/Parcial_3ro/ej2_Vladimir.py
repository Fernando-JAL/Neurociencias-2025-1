'''
# EJERCICIO 2:
Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:
- ¿Qué forma tiene el grafo?
    El grafo tiene la forma de un dodecaedro(poliedro de doce caras)

- ¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
    El numero de nodos es de 20, para conocerlo podemos hacerlo de diferentes maneras. Sin embargo, la manera mas sencilla es print(G.number_of_nodes()), donde la funcion de networkx number_of_nodes() nos devuelve el numero de nodos del grafo G.

- ¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de nodo
    El numero de aristas es de 30, la funcion Graph.number_of_edges() de networkx nos permite conocerlo. En este caso es print(G.number_of_edges()).

- ¿Qué hace el código G.degree?
    Esta funcion de networkx nos devuelve el conjunto (nodo, grado) de un grafo para con todos sus nodos.

- ¿Cuál es el número máximo de aristas en el grafo?
    Matematicamente es posible conocer el numero maximo de aristas del grafo (dado que se trataria de un grafo completo no dirigido), para ello utilizamos la formula N(N-1)/2 para nuestro nodo. 20(20-1)/2  = 190 aristas.

- ¿Cuál es la diferencia entre animation2_1 y animation2_2?
    Principalmente la presencia de la animacion de giro en animation2_2 y no en animation2_1

'''