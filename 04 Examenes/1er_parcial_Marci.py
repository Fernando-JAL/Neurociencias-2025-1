# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

# n debe ser mayor a 0 !!!!!!

# def fibonacci(n):
#     n=n
#     i1 = 1
#     i2 = 1
#     for x in range(n-2):
#         i = i1 + i2
#         i1 = i2
#         i2=i
#     print('El término', n, 'es',i2)
#
# # por definición de fibonacci n debe ser mayor a 2 (los primeros dos términos son 1)
# fibonacci(4)



# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

# def fibonacci(n):
#     n=n
#     if n==1:
#         print('El término 1 es 1 La secuencia es: [1]'),
#     else:
#         i1 = 1
#         i2 = 1
#         f = [i1, i2]
#         for x in range(n-2):
#             i = i1 + i2
#             i1 = i2
#             i2=i
#             f.append(i)
#         print('El término', n, 'es',i2, 'La secuencia es:', f)
# fibonacci(9)






# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

# def how_many_squares(a, b):
#     count = 0
#     for i in range(1, b + 1):
#         if a <= (i * i) <= b:
#             count += 1
#     print(count)
#
# how_many_squares(2,25)








# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

# def how_many_a(s,n):
#     str(s)
#     int(n)
#     s = s[:n]
#     print(s)
#     print(s.count('a'))
#
# how_many_a('manzanaaaaaanaaa',10)








# 5. Dada una lista de enteros que representan las longitudes de bastones, debes iterativamente cortar los bastones en
# bastones más cortos descartando las piezas más cortas hasta que no queden ninguna. En cada iteración debes determinar
# la longitud del bastón más corto. Cuando los bastones remanentes son de la misma longitud, no pueden ser recortados más
# entonces se descartan.
#
# - Crear una función que reciba una lista de enteros, y retorne el número de bastones en cada iteración
#
# Ejemplo:
# Entrada: [5, 4, 4, 2, 2, 8]
# Salida: [6, 4, 2, 1]
#
# Explicación:
# longitud de bastones    longitud a cortar   bastones recortados
# 5 4 4 2 2 8             2               6
# 3 2 2 _ _ 6             2               4
# 1 _ _ _ _ 4             1               2
# _ _ _ _ _ 3             3               1
# _ _ _ _ _ _           Terminado         Terminado

# ESCRIBE TU CÓDIGO AQUÍ

# def bastones(x):
#     output = []
#     while sum(x) > 0:
#         output.append(len(x))
#         min_val = min(x)
#         for i in range(len(x)):
#             x[i] = x[i] - min_val
#         for i in range(x.count(0)):
#             x.remove(0)
#     print(output)
#
#
# bastones([5, 4, 4, 2, 2, 8])






