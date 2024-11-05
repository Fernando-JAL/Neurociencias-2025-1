# Primero

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Introduce el valor de n: "))

resultado = fibonacci(n)
print(f"El término {n}-ésimo de la serie de Fibonacci es: {resultado}")

# Segundo

n = int(input("Introduce el valor de n para los primeros términos de la serie de Fibonacci: "))
for i in range(1, n + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Tercero

import math


def contar_cuadrados_enteros(a, b):
    raiz_a = math.ceil(math.sqrt(a))
    raiz_b = math.floor(math.sqrt(b))

    if raiz_b >= raiz_a:
        return raiz_b - raiz_a + 1
    else:
        return 0


a = int(input("Introduce el valor inicial (a): "))
b = int(input("Introduce el valor final (b): "))

resultado = contar_cuadrados_enteros(a, b)
print(f"El número de cuadrados enteros en el rango [{a}, {b}] es: {resultado}")


# Cuarto

def contar_a_en_cadena_infinita(s, n):
    cuenta_a_s = s.count('a')

    repeticiones_completas = n // len(s)

    total_a = repeticiones_completas * cuenta_a_s

    letras_sobrantes = n % len(s)

    total_a += s[:letras_sobrantes].count('a')
    return total_a


cadena = input("Introduce la cadena de letras en minúscula: ")
n = int(input("Introduce el número de letras a considerar: "))

resultado = contar_a_en_cadena_infinita(cadena, n)
print(f"El número de 'a' en las primeras {n} letras de la cadena infinita es: {resultado}")


# Quinto

def cortar_bastones(bastones):
    resultados = []

    while len(bastones) > 0:
        resultados.append(len(bastones))
        minimo = min(bastones)
        bastones = [b - minimo for b in bastones if b - minimo > 0]

    return resultados


bastones = list(map(int, input("Introduce las longitudes de los bastones separadas por espacios: ").split()))
resultados = cortar_bastones(bastones)
print("Número de bastones en cada iteración:", resultados)
