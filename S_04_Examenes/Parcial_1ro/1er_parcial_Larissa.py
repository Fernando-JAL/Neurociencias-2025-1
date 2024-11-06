# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia: $F(n) = F(n-1) + F(n-2)$
# donde n\in\mathbb{N} es el n-ésimo término de la serie de Fibonacci
# y los primeros términos son: F(1) = 1 y F(2) = 1.

# - Crear una función que reciba un entero n y devuelva el $n$-ésimo término de la serie de Fibonacci.
def fibonacci_recursivo(n):
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
print(fibonacci_recursivo(7))

# # - Recibir por teclado un número n y devuelva el n-ésimo término de la serie de Fibonacci.
def fibonacci_recursivo(n):
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

n = int(input("Introduce un número entero n: "))

resultado = fibonacci_recursivo(n)

print(f"El {n}-ésimo término de la serie de Fibonacci es: {resultado}")


# # Utilizando la función del ejercico anterior, recibir por teclado un entero
# # n e imprimir los n-ésimos términos de la serie de Fibonacci.
def fibonacci_recursivo(n):
    if n <= 0:
        return "El número debe ser mayor que 0"
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

n = int(input("Introduce un número entero n: "))
if n <= 0:
    print("El número debe ser mayor que 0")
else:
    print(f"Los primeros {n} términos de la serie de Fibonacci son:")
    for i in range(1, n + 1):
        print(fibonacci_recursivo(i), end=" ")

# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
# - Crear una función que reciba dos enteros: a y b y retorne el número de cuadrados enteros en el rango [a, b]

def cuadrados_enteros (a, b):
    if a > b:
        return 0
    z = 1
    calculadora = 0

    while z * z < a:
        z += 1
    while z * z <= b:
        calculadora += 1
        z += 1
    return calculadora

a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
resultado = cuadrados_enteros(a, b)
print(f"El número de cuadrados enteros en el rango [{a}, {b}] es: {resultado}")

# 4. Sea una cadena s de letras en minúscula q se repite infinitamente. Dado un entero n, encuentra e
# imprime el número de letras 'a' en las primeras n letras de la cadena infinita.
# - Crear una función que reciba la cadena s y el entero n y retorne el número de 'a's en las primeras n letras de
# la cadena infinita.
# - Recibir por teclado la cadena s y el entero n.

s = "pinpon es un muñeco muy guapo y de cartón se lava su carita con agua y con jabón se desenrreda el pelo con peine de marfil y aunque se de tirones no llora ni hace así"
def cadena_infinita(s, n):
    n = min(n, len(s))
    count_a = s[:n].count('a')
    return count_a

n = int(input("Introduce el número de letras n: "))
resultado = cadena_infinita(s, n)
print(f"El número de letras 'a' en las primeras {n} letras de la cadena es: {resultado}")

# 5. Dada una lista de enteros que representan las longitudes de bastones, debes iterativamente cortar los bastones en
# bastones más cortos descartando las piezas más cortas hasta que no queden ninguna. En cada iteración debes determinar
# la longitud del bastón más corto.
# Cuando los bastones remanentes son de la misma longitud, no pueden ser recortados más
# entonces se descartan.
# Crear una función que reciba una lista de enteros, y retorne el número de bastones en cada iteración

# Ejemplo:
# Entrada: [5, 4, 4, 2, 2, 8]
# Salida: [6, 4, 2, 1]

# Explicación:
# longitud de bastones    longitud a cortar   bastones recortados
# 5 4 4 2 2 8             2               6
# 3 2 2 _ _ 6             2               4
# 1 _ _ _ _ 4             1               2
# _ _ _ _ _ 3             3               1
# _ _ _ _ _ _           Terminado         Terminado

string_examen = "ya no me alcanzó el tiempo profe."