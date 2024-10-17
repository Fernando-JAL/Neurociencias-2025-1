# Operaciones básicas
# La clase array es muy flexible y permite muchas operaciones entre dos arrays,
# aunque con algunos requisitos.
#
# Suma
# Por ejemplo las operaciones suma y resta requieren que los arrays tengan la
# misma forma, es decir, mismo número y tamaño de las dimensiones.
import numpy as np

lista1 = list(range(5))
lista2 = [11, 12, 13, 14, 15]

array1 = np.array(lista1)
array2 = np.array(lista2)
print(array1.shape, array2.shape)

print('suma de listas:', lista1 + lista2)
print('arrays:', array1, array2)
print('suma de arrays:', array1 + array2)

print('La suma de array TIENE que tener la misma forma')
# print('suma', np.array([1, 2, 3]) + np.array([5, 6]))
print('resta de arrays:')
print('resta', np.array([1.5, -2, 13.21]) - np.array([5.25, 6, 1]))

# producto de array por constantes
c = 6.5
array = np.array([3, 4, 6, 8, 12])
print('producto por constante', c*array, array*2)

# Producto
# En el caso del producto, la divisón y la potencia se pueden operar arrays
# de las mismas dimensiones si el número de columnas de la primera coincide
# con el número de filas de la segunda:
# Dos arrays
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([2,3,4,5])

# Los multiplicamos
print('producto por arrays:', arr_1 * arr_2)

# División
# Igual que el producto, la división entre arrays se basa en dividir cada
# elemento de un array por el elemento en la misma posición del otro:

arr_1 = np.array([12, 14, 16, 18, 30])
arr_2 = np.array([3, 7, 12, 2, 10])

print('division por array', arr_1/arr_2)

print('division por constante', arr_1/2)

print('division constante sobre array', 10/arr_1)

print('potencia de array', arr_2**2)

print('potencia de array', arr_2**0.5)

print("""NOTA: no es posible arr_2**(-2), 
pero es equivalente a 1/arr_2**2""", 1/arr_2**2)
print('o equivalentemente, especificar la potencia como float', arr_2**(-2.))

# potencia entre arreglos
# Potencia
# Como es normal, se basa en realizar la potencia entre los valores que
# comparten posición en los arrays:
#
# arr_1, arr_2
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([2,3,4,5])
print('potencia entre arreglos', arr_1**arr_2)

