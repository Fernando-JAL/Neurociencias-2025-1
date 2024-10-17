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
