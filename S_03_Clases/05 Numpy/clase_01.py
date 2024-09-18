# La clase array de NumPy
# La programación gráfica se basa en la idea de manipular información almacenada
# en unas estructuras conocidas como vectores y matrices.
#
# En Python la única forma de simular estas estructuras es usando listas y
# lo malo es que son muy limitadas respecto a las funciones matemáticas
# que permiten.
#
# Numpy viene a solucionar esa carencia ofreciéndonos un nuevo tipo
# de dato llamado array, es parecido a una lista y de hecho se puede crear a
# partir de ellas:

# RECORDANDO LISTAS
lista1 = [2, 3, 4, 5, 6]
lista2 = [2, 3, 4, 5, 6]

print(lista1)

# ARREGLOS
import numpy as np
# arreglos unidimensionales
lista1 = [2, 3, 4, 5, 6]
array = np.array(lista1)
print(array)
print(type(array))

print(len(lista1))
print(len(array))
print(array.ndim)   # dimension del arreglo
print(array.shape)  # forma del arreglo

# arreglos bi dimensionales
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
    ])
print('arreglo:', array)
print('dimension del arreglo', array.ndim)
print('forma del arreglo', array.shape)


