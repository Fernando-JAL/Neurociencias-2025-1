#Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:

#¿Qué forma tiene el grafo?
    #Ambos son dodecaedros
#¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
    # En ambos códigos, el número de nodos es 20
    # Se hace con el código:
        # num_nodos = G.number_of_nodes()
        # print('Número de nodos:', num_nodos)

#¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de nodos?
    # En ambos códigos e número de aristas es 30
    # Lo hice con el código:
        # num_aristas = G.number_of_edges()
        # print('Número de aristas:', num_aristas)

#¿Qué hace el código G.degree()?
    # Calcula el grado de todos los nodos. Se puede devolver con el formato (nodo, grado) si ponemos el código así:
        #for nodo, grado in G.degree():
        # print(f'Nodo {nodo} tiene grado {grado}')

#¿Cuál es el número máximo de aristas en el grafo?
    # 190!!
    # Código:
            # def max_aristas(n):
        #     return n * (n-1) // 2
        # n = 20
        # print('Máximo de número de nodos:', max_aristas(n))

#¿Cuál es la diferencia entre animation2_1 y animation2_2?
    # Que en el código de 'animation2_2' tiene la parte de:

# def animate(i):
#     ax.view_init(elev=20, azim=i*4)
#     return fig,
#
# ani = animation.FuncAnimation(fig, animate, init_func=init, frames=90, interval=200, blit=False)
# plt.show()

    # Eso hace que rote el gráfico