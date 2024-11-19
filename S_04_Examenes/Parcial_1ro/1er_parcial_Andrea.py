# Examen primer parcial
# Andrea Mercado Jiménez
# 9 septiembre 2024

# Examen primer parcial
# Andrea Mercado Jiménez
# 9 septiembre 2024


# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
def fibonacci(n):
  if n <= 0:
    return "El índice debe ser un número entero positivo."
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese el índice del término de Fibonacci que desea calcular: "))

resultado = fibonacci(n)
print("El término", n, "de la serie de Fibonacci es:", resultado)


#2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

def fibonacci(n):
  if n <= 0:
    return "El índice debe ser un número entero positivo."
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Ingrese la cantidad de términos de la serie de Fibonacci que desea calcular: "))

print("Los primeros", n, "términos de la serie de Fibonacci son:")
for i in range(1, n+1):
  print(fibonacci(i), end=" ")


# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número de cuadrados enteros en el rango $[a, b]$

def contar_cuadrados_perfectos(a, b):
  contador = 0
  for i in range(int(a**0.5), int(b**0.5) + 1):
    cuadrado = i * i
    if a <= cuadrado <= b:
      contador += 1
  return contador

print(contar_cuadrados_perfectos(3, 3))
print(contar_cuadrados_perfectos(9, 9))
print(contar_cuadrados_perfectos(1_000_000, 9_000_000))
# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

def contar_as(s, n):
  longitud_cadena = len(s)
  repeticiones_completas = n // longitud_cadena
  as_en_repeticiones_completas = repeticiones_completas * s.count('a')
  resto = n % longitud_cadena
  as_en_resto = s[:resto].count('a')
  return as_en_repeticiones_completas + as_en_resto

s = input("Ingrese la cadena base: ")
n = int(input("Ingrese el número de letras a considerar: "))

resultado = contar_as(s, n)
print("Hay", resultado, "letras 'a' en las primeras", n, "letras de la cadena.")


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







