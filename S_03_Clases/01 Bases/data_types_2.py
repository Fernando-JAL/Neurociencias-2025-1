# This script is to describe the data types used in python. Part 2 Sequence

# list. Tipo compuesto de dato que puede almacenar distintos elementos
# (llamados ítems) ordenados entre [ ] y separados con comas.

#Ejemplo 1
list1 = [2, 4, 7]
print('list1 es de tipo:', type(list1))

#Ejemplo 2
list2 = [2, -17/3, complex(3, 7.5), 5-7j, 'chain']
print('Lista list2 = ', list2)
print('El tipo de dato de list2 es:', type(list2))

#Ejmplo 3
list3 = ['tomate', 'aguacate', 'papa']
list4 = ['lobo', 'jiraga', 'tigre', 5, 'oso']
list5 = ['ocho', 19.2, [45, 'paz'], -4, 5+8]
print('list5 = ', list5)
print('list5 es de tipo:', type(list5))

#SLICING

print('Ejemplo de slicing:', list5[3])
print('Ejemplo de slicing en list5:', list5[-1])
print('Ejemplo de slicing en list5:', list5[2])
print('Ejemplo de doble slicing usando list', list5[2][1])
print('Ejemplo de doble slicing usando list', list5[2][0])

# Pregunta: Es válido el doble slicing en list5[0]?
print('Ejemplo de doble slicing usando list', list5[0][3])

# Operaciones con listas. Suma de listas
print(list2, list3)
print('Sumando las listas list2 y list3, se obtiene:\n', list2+list3)
print('Sumando las listas list3 y list2, se obtiene:\n', list3+list2)

list1 = [2, 4, 'lobo']
print('list1 = ', list1)
# Producto por escalar
print('3*list1 = ', 3*list1)
print('list1*3 = ', list1*3)

list_ = list3 + 2*list1
print(list_)
# Lst[ Initial : End : IndexJump ]
print(list_[1:5])
print(list_[0:-1:2]) #['tomate', 'aguacate', 'papa', 2, 4, 'lobo', 2, 4]
print(list_[::2])
print(list_[::-1])

# Las listas son modificables
print('list_ = ', list_)
list_[5] = 'gato'
print(list_)
# Como alternativa a buscar el índice del elemento de interés,
# podemos utilizar el metodo index
print("Obteniendo el índice del elemento 'gato':", list_.index('gato'))
print("Obteniendo el índice del elemento 2:", list_.index(2))

# Agregar valores a una lista usando el metodo append
print(list_)
list_.append(5)
print(list_)

list_ = list_ + [9]
print(list_)

# Para insertar un valor en una posición en específico
# se usa el método insert
list_.insert(28, ['rosa', 'amarillo', 'azul', 'blanco', 'y ya'])
print(list_)

# Función len()
print('Para determinar el número de elementos de list_,'
      '\nse usa len y se obtiene como resultado:', len(list_))

# A partir de strings se pueden crear listas
texto = 'el día de hoy ya se quieren ir de la clase xq los niños ya están cansaditos y se quieren mimir'
print(texto.split())
print(type(texto.split()))

# Eliminar elementos de listas
# Eliminando elementos por valor
print(list_)
list_.remove('papa')
print(list_)
# Eliminando elementos por índice
print(list_)
list_.pop(4)
print(list_)
list_.pop()
print(list_)
