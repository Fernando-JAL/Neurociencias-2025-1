# EXAMEN
# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

##1.1 Para un n determinado inicialmente
print('Ejercicio 1.1')
def fibonacci(n):
    if n <= 0:
        return "n debe ser > 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 5
print("El n-ésimo término de la serie de Fibonacci es:", fibonacci(n))

##1.2
#ahora, el código pero si por teclado se introduce el valor de n

print('Ejercicio 1.2')
def fibo(z):
    if z <= 0:
        return "n debe ser > 0."
    elif z == 1:
        return 0
    elif z == 2:
        return 1
    else:
        return fibonacci(z-1) + fibonacci(z-2)

z = int(input('Escribe el valor de z:'))
print("El n-ésimo término de la serie de Fibonacci es:", fibonacci(z))


# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ
print('ejercicio 2')

def fib(p):
    if p <= 0:
        return "p debe ser mayor que 0."
    elif p == 1:
        return 0
    elif p == 2:
        return 1
    else:
        return fib(p-1) + fib(p-2)

p = int(input("Introduce el valor de p: "))

print("Los", p, "términos de la serie de Fibonacci son:")
for i in range(1, p+1):
    print(fib(i))


# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

print('ejercicio 3')
def squares(start, end):
    cuadrados = []
    q = 1

    while q ** 2 <= end:
        cuadrado = q ** 2
        if cuadrado >= start:
            cuadrados.append(cuadrado)
        q += 1

    return cuadrados


start = int(input("Introduce el número inicial del rango: "))
end = int(input("Introduce el número final del rango: "))

resultado = squares(start, end)
print("Los cuadrados enteros que existen dentro del rango son:", resultado)


# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

print('ejercicio 4')
def kadena(cadena, w):
    repeticiones_completas = w // len(cadena)
    sobrante = w % len(cadena)

    a_en_cadenas_completas = cadena.count('a') * repeticiones_completas
    a_en_cadena_sobrante = cadena[:sobrante].count('a')

    return a_en_cadenas_completas + a_en_cadena_sobrante

s = input("Introduce la cadena de letras en minúscula: ")
w = int(input("Introduce el entero w: "))

res = kadena(s, w)
print("El número de letras 'a' en las primeras", w, "letras de la cadena es:", res)


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

print('ejercicio 5')

def ej_bastones(bastones):
    bota = []

    while bastones:
        bota.append(len(bastones))

        menor_baston = bastones[0]
        for baston in bastones:
            if baston < menor_baston:
                menor_baston = baston

        listados = []
        for baston in bastones:
            nuevo_baston = baston - menor_baston
            if nuevo_baston > 0:
                listados.append(nuevo_baston)
        bastones = listados

    return bota

bastones_input = input("Introduce las longitudes de los bastones:")

bastones = []
num = ""
for bo in bastones_input:
    if bo == " ":
        if num:
            bastones.append(int(num))
            num = ""
    else:
        num += bo
if num:
    bastones.append(int(num))

bota = ej_bastones(bastones)
print("Salida:", bota)

print('póngame 100 por favor :)')