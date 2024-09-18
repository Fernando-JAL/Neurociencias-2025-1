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

def fibonacci2(n: int) -> int:
    if (n == 1) or (n == 2):
        return 1
    numeros = [1, 1]
    for i in range(2, n):
        fib = numeros[i-1] + numeros[i-2]
        numeros.append(fib)
    return numeros[-1]

def fibonacci3(n: int) -> int:
    if n < 1:
        print('fibonacci solo es válido para n >= 1')
        return
    numeros = [1, 1]
    if n-1 < len(numeros):
        return numeros[n-1]
    return fibonacci3(n-1) + fibonacci3(n-2)

# print(fibonacci2(2500))
# valor = int(input('Introduce un entero n, para calcular el n-ésimo término de fibonacci: '))
# print(fibonacci(valor))

# Pruebas a realizar:
# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(25) = 75025
# fibonacci(-5) = 1 ó no valido
# fibonacci(2500) = 1317090516751949629522763087125316412066606964992507141887746936727530870405038425764503130123186407746570862185871925952766836352119119528156315582632460790383834605654880612657718465632568839245978248473058179422070735553124716385450886640552392273856770672239797164264356927661308349671941673643205733343592701716715788255170679575500279186053316365583259186927359351023387298371686222860827415371...
            # se acepta que no de resultado



# --------------------------------------------------------------------------------------
# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

# valores = int(input('Introduce un entero n, para calcular los n términos de fibonacci: '))
# for valor in range(1, valores+1):
#     print(fibonacci2(valor), end=" ")

# Pruebas a realizar:
# fibonacci(1) = 1
# fibonacci(2) = 1
# fibonacci(25) = 75025
# fibonacci(-5) = 1 ó no valido
# fibonacci(2500) = 1317090516751949629522763087125316412066606964992507141887746936727530870405038425764503130123186407746570862185871925952766836352119119528156315582632460790383834605654880612657718465632568839245978248473058179422070735553124716385450886640552392273856770672239797164264356927661308349671941673643205733343592701716715788255170679575500279186053316365583259186927359351023387298371686222860827415371...
            # se acepta que no de resultado



# --------------------------------------------------------------------------------------
# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlock debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número de cuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

import math
def cuadrados_enteros(a: int, b: int) -> int:
    contador = 0
    for val in range(a, b+1):
        if val**0.5 % 1 == 0:
            contador += 1
    return contador

def cuadrados_enteros2(a: int, b: int) -> int:
    if a < 0 or b < 0:
        print('Los valores a y b deben ser enteros positivos ')
        return
    sqrt_a = math.ceil(a ** 0.5)
    sqrt_b = math.floor(b ** 0.5)
    return len(range(sqrt_a, sqrt_b+1))

# print(cuadrados_enteros2(4, 65))

# Pruebas a realizar
# cuadrados_enteros(4, 65) = 7
# cuadrados_enteros(3, 3) = 0
# cuadrados_enteros(9, 9) = 1
# cuadrados_enteros(1_000_000, 9_000_000) = 2001



# --------------------------------------------------------------------------------------
# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

def cadena_infinita(s: str, n: int) -> int:
    longitud = len(s)
    multiplos = (n//longitud + 1)
    cadena_extendida = s * multiplos

    return cadena_extendida[:n].count('a')


def cadena_infinita2(s: str, n: int) -> int:
    if len(s) >= n:
        return s[:n].count('a')
    multiplos = n//len(s)
    residuo = n%len(s)

    return multiplos*s.count('a') + s[:residuo].count('a')


# s, n_char = input('Introduce la cadena y el entero:').split()
# n_ = int(n_char)
# print(cadena_infinita(s, n_))

# Pruebas a realizar
# cadena_infinita('a', 1_000_000_000) = 1_000_000_000
# cadena_infinita('cabaña en la mañana', 8) = 3
# cadena_infinita('cabaña en la mañana', 0) = 0
# cadena_infinita('cabaña en la mañana', 19) = 7
# cadena_infinita('cabaña en la mañana', 190) = 70


# --------------------------------------------------------------------------------------
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

def recorte_de_bastones(bastones: list) -> list:
    bastones_recortados = []
    while len(bastones) > 0:
        bastones_recortados.append(len(bastones))
        aux = []
        for baston in bastones:
            if baston != min(bastones):
                aux.append(baston)
        bastones = aux

    return bastones_recortados

print(recorte_de_bastones([5, 4, 4, 2, 2, 8]))

# Pruebas a realizar
# recorte_de_bastones([1, 2, 3]) = [3, 2, 1]
# recorte_de_bastones([5, 4, 4, 2, 2, 8]) = [6, 4, 2, 1]
# recorte_de_bastones([1, 2, 3, 4, 3, 3, 2, 1]) = [8, 6, 4, 1]
