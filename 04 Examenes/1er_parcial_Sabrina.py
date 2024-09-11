# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ
# FUNCIÓN 1
def fibo1(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)
res1 = fibo1(5)
print(f'El {5}-ésimo término de la serie de Fibonacci es: {res1}')

# FUNCION 2
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('Introduzca el número: '))
res = fibo(n)
print(f'El {n}-ésimo término de la serie de Fibonacci es: {res}')




# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.
# ESCRIBE TU CÓDIGO AQUÍ
def fibo2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo2(n-1) + fibo2(n-2)
n = int(input('Introduzca el número: '))
fibonacci_lista = [fibo2(i) for i in range(1, n + 1)]
print(f'Los primeros {n} términos de la serie de Fibonacci son: {fibonacci_lista}')


# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$
# ESCRIBE TU CÓDIGO AQUÍ
def cuad_e(a, b):
    inicio = int(a ** 0.5)
    fin = int(b ** 0.5)
    if inicio ** 2 < a:
        inicio += 1
    if fin >= inicio:
        return fin - inicio + 1
    else:
        return 0
a = int(input('Introduce el valor inicial: '))
b = int(input('Introduce el valor final: '))
fin = cuad_e(a, b)
print(f'Número de cuadrados enteros en el rango [{a}, {b}] es: {fin}')

# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.
# ESCRIBE TU CÓDIGO AQUÍ
def letras(palabra):
    if len(palabra) == a:
        print('palabra:', palabra)
        palabra = palabra [:-1]
        letras(palabra)
    else:
        print('palabra nula', palabra)
    print(c.lower('saliendo de la función,', len(palabra)))
letras('abc')


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