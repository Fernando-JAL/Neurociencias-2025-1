# tipos de datos boleanos
# Los tipos de dato boleano representan uno de dos posibles valores: True o False

valor1 = True # TRUE
valor2 = False
print('tipos de valores boleanos:', valor1, valor2)
print('usando type:', type(valor1), type(valor2))

print('usando and', valor1 and valor2)
print('usando or', valor1 or valor2)

# Conversiones a boleano
print('entero 0 a boleano', bool(0))
print('entero 1 a boleano', bool(1))
print('entero 5 a boleano', bool(5))
print('entero -7.5 a boleano', bool(-7.5))

# Conversiones a boleano de strings
print("str '' a boleano", bool(''))
print("str ' ' a boleano", bool(' '))
print("str 'a' a boleano", bool('a'))
# cadena nula: ''

print('lista vacía [] a boleano', bool([]))
print('tupla vacia () a boleano', bool(()))
print('diccionario vacío {} a boleano', bool({}))

# DICCIONARIO {}
# Los diccionarios son usados para almacenar datos en formatos key: value
diccionario1 = dict()
print('ej de diccionario:', diccionario1, 'su tipo es:', type(diccionario1))

diccionario1 = {'llave1': 'lobo', 'llave2': -82.654, 34: 'cosa', 'llave4': [2, 3, 4]}
print('diccionario1', diccionario1)

# slicing a diccionario
print('para el slicing uso la llave')
print(diccionario1['llave2'])
print(diccionario1['llave4'])
print(diccionario1[34])

print('Usando len, el diccionario tiene:', len(diccionario1), ' elementos')


# Sets
# Los conjuntos son una colección de valores no ordenados que no admiten duplicados
# entre { } y separados con comas
set1 = {3, 6, 'azul'}
print('Ej de conjunto:', set1, 'de tipo:', type(set1))

set1 = {3, 'jaja', 8, 12, 8, 'jaja', 'jeje', 3, 12}
print('Ej de conjunto:', set1)


print('index de un set', set1 + {4, 5, 6})



