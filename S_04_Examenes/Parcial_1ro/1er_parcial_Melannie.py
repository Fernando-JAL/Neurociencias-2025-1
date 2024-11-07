# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#$F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
aaaaaaa

# Escribe tu código aquí
def fibonacci(n):
    if n <= 0:
        return "no valido"
    #no sé si aquí tambien se le pueda poner un elif o
    # else para que no aparezca el mensaje junto pero no me salió
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
n = int(input("Introduce un valor para n: "))
print(f"El {n}-ésimo término de la serie de Fibonacci es: {fibonacci(n)}")


# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

def primeros(n):
    x = []
    for i in range(1, n + 1):
        x.append(fibonacci(i))
    return x

n = int(input("Introduce número de términos: "))
print("Primeros", n, "términos de la serie son:")
print(primeros(n))

# 3. A Watson le gusta retar la habilidad matemática de Sherlock.
# Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlock debe determinar
# el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
##NO ME SALEEEEEEEEEEEEEEE, YA ME HARTÉ, NO LE ENTIENDO, me rindo.
# - Crear una función que reciba dos enteros:
# $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$


#cuadrados_c= 0
#def cuadrados_enteros(a, b):
 #   num = 1
  #  while num * num < a:
   #     num += 1


    #while num * num <= b:
     #cuadrados_c += 1
  #  num += 1

    #return cuadrados_c
# print(cuadrados_enteros(a, b))

import math


def cuadrados_enteros(a, b):
    if a > b:
        return 0

    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))

    return max(0, end - start + 1)


a = int(input("Escribe el valor para a: "))
b = int(input("Escribe el valor para b: "))
print(f"Cantidad de cuadrados enteros en el rango [{a}, {b}] es: {cuadrados_enteros(a, b)}")


# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.
def a_en_palabra(s, n):
    longitud_s = len(s)
    count_a_in_s = s.count('a')

    rs = n // longitud_s
    rs = n % longitud_s

    count_a = rs * count_a_in_s
    count_a += s[:r].count('a')

    return count_a

s = input("Introduce una cadena en minúsculas: ")
n = int(input("Número de n: "))
print(f"El número de 'a' en las primeras {n} letras es: {a_en_palabra(s, n)}")









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