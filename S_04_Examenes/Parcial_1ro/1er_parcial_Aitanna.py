# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def ser_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

n = int(input("Introduce un número entero: "))
if n > 0:
    print(ser_fibonacci(n))


# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def ser_comp(n):
    ser = [ ]
    for i in range(1, n +1):
        ser.append(ser_fibonacci(i))
    return ser

n_total = int(input("Introduce un número entero: "))
if n_total > 0:
    ser = ser_comp(n)
    print(ser)

# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

def cuadrados(a, b):
    menor = int(a ** 0.5)
    if menor ** 2 < a:
        menor += 1
    mayor = int(b ** 0.5)
    if mayor > menor:
        return mayor - menor + 1

a = int(input("Introduce un número entero: "))
b = int(input("Introduce otro número entero mayor al anterior: "))
print(cuadrados(a, b))







# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

def contar_a(s, n):
    contar_as = s.count("a")
    len_s = len(s)
    total_a = s.count("a") // len_s
    return total_a

s = input("Introduce una cadena de texto: ")
n = int(input("Introduce un número entero: "))

print(contar_a(s, n))






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





