# TUPLAS
# Es una colección de elementos distintos ordenados entre ( ) y separados por comas.

tupla = (3, 2, 'ocho')
print('La tupla:', tupla, 'es de tipo:', type(tupla))

#como característica principla de las tuplas, cuando tenemos una tupla con 1 elemento
tupla = ('5')
print('La tupla de 1 elemento es:', tupla, 'es de tipo:', type(tupla))

#verdadera forma de definir una tupla con 1 elemento
tupla = ('5',)
print('La tupla de 1 elemento es:', tupla, 'es de tipo:', type(tupla))
print('Su cantidad de elementos es:', len(tupla))

#Slicing
tupla = (3, 6, 'ocho', 'lobo', 'chocolate', 'tierra', [9.2], 'cosa')
print('tupla:', tupla)
print('aplicando slicing:', tupla[4])
print('aplicando slicing con números negativos:', tupla[-4: -1])

#Mutabilidad
#tupla[3] = 'cachorro'
#print('Tupla mutable', tupla)
#conclusión: las tuplas son no mutables

#suma de tuplas
tupla1, tupla2 = (1, 2, 3), ('cosa', 'casa', 'ronquido')
print('suma de tuplas:', tupla1 + tupla2)
print('aplicando la función len:', len(tupla1+tupla2))
print('multiplicando tuplas por un entero:', tupla1*4)

#convertir tuplas a listas
print('convirtiendo tupla a lista:', list(tupla1), 'tiene tipo:', type(list(tupla1)))

#convertir listas a tuplas
print('convirtiendo lista a tupla:', tuple(['azul', 'oso']),
      'tiene tipo:', type(tuple(['azul', 'oso'])))

# a manera de resumen:
# mutabilidad
# operaciones con tuplas: suma, producto por un entero
# slicing
# converción de tuplas a listas y viceversa

# RANGOS.
# La función range() retorna una sucesión de numeros en un rango, range(start, stop, step)
rango1 = range(5)
print('ejemplo de rango:', rango1, 'rango1 es de tipo:', type(rango1))

#conversión de range a lista
print('convirtiendo el rango a lista:', list(rango1))

rango2 = range(3, 104, 3)
print('convirtiendo el rango a lista:', list(rango2))

print('apicando slicing al rango con 1 elemento:', rango2[0],
      '\ncon múltiples elementos', rango2[2: 5])

# diccionario!!!!


