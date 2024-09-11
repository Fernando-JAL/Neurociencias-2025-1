# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def fibonacci(n: int) -> int:
    if n < 1:
        print('fibonacci solo es válido para n >= 1')
        return 0
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    if (n == 1) or (n == 2):
        return 1
    numeros = [1, 1]
    for i in range(2, n):
        fib = numeros[i-1] + numeros[i-2]
        numeros.append(fib)
    return numeros[-1]

# print(fibonacci2(-5))

# valor = int(input('Introduce un entero n, para calcular el n-ésimo término de fibonacci: '))
# print(fibonacci(valor))


# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

# valores = int(input('Introduce un entero n, para calcular los n términos de fibonacci: '))
# for valor in range(1, valores+1):
#     print(fibonacci(valor))






# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlock debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número de cuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

def cuadrados_enteros(a, b):
    contador = 0
    for val in range(a, b+1):
        if val**0.5 % 1 == 0:
            contador += 1
    return contador

# print(cuadrados_enteros(4, 25))


# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

def cadena_infinita(s, n):
    longitud = len(s)

    multiplos = (n//longitud + 1)
    cadena_extendida = s * multiplos

    return cadena_extendida[:n].count('a')

s, n_char = input('Introduce la cadena y el entero:').split()
n = int(n_char)
print(cadena_infinita(s, n))


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






