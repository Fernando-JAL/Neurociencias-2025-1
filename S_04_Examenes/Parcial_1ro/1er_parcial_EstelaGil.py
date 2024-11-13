# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
# F(n) = F(n-1) + F(n-2), donde n es el n-ésimo término de la serie de Fibonacci y
# los primeros términos son: F(1) = 1 y F(2) = 1.
# a) Crear una función que reciba un entero n y
# devuelva el n-ésimo término de la serie de Fibonacci.

def serie_fibonnacci(n):
    if n == 1 or n == 2:
       return 1
    else:
       return serie_fibonnacci(n-1) + serie_fibonnacci(n-2)

print('la posición corresponde a: ', serie_fibonnacci(10))

# b) Recibir por teclado un número n y devuelva el n-ésimo término de la serie de Fibonacci.
def serie_fibonnacci(n):
  if n == 1 or n == 2:
     return 1
  else:
     return serie_fibonnacci(n-1) + serie_fibonnacci(n-2)

numero = int(input('escribe un número entero: '))
respuesta = serie_fibonnacci(numero)
print('el término ', numero, 'de la serie es: ', respuesta)

# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero n e imprimir los n-ésimos términos de
# la serie de Fibonacci.

def serie_fibonnacci(n: int):
    if n == 1 or n == 2:
     return 1
    else:
     return serie_fibonnacci(n-1) + serie_fibonnacci(n-2)

number = int(input('escribe un número entero: '))
for i in range(1, number+1):
    print('los términos de la serie: ',i, serie_fibonnacci(i))

# 3. A Watson le gusta retar la habilidad matemática de Sherlock.
# Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlock debe determinar el número de cuadrados enteros dentro del rango.
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

def funcion_enteros(a, b: int):
    primero = int(a**0.5)
    for idx in range(1, 100):
        if idx **0.5 == int:
           return

# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras n letras de la cadena infinita.
# - Crear una función que reciba la cadena s y el entero $n$ y retorne el número de 'a's en las primeras n letras de
# la cadena infinita.
# - Recibir por teclado la cadena s y el entero n

def cadenita(s: str, n: int) -> int:
    contar_as= s.count('a')
    repeticiones = n//len(s)
    letras_sobrantes = n%len(s)
    contar_as_sobrantes = s[:letras_sobrantes]
    as_totales = contar_as_sobrantes + contar_as * repeticiones
    return as_totales

s = str(input('introduce una cadena de letras minúsculas: '))
n = int(input('introduce un número de letras: '))
contar_as= s.count('a')
respuesta = contar_as(s, n)
print('el número de letras A en las primeras n letras: ', respuesta)

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