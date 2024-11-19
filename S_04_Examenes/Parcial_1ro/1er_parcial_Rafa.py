# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
from typing import final


# ESCRIBE TU CÓDIGO AQUÍ


def fib(n):

    numero1 = 0
    numero2 = 0
    siguiente = 1
    final = 0

    for idx in range(0,n):

       final = siguiente
       numero1 = numero2
       numero2 = siguiente
       siguiente = numero1 + numero2
    return final


valor = input("Introduce un número: ")
print(fib(int(valor)))


# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ







# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. Sherlos debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

def contar(a, b):

    contador = 0
    val = 1

    #Llegar hasta a
    while val * val < a:
        val += 1

    #Contar
    while val * val <= b:
        contador += 1
        val += 1

    return contador

#Ejemplo
print(contar(16,17))



# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

def contarcadena(cadena, longitud):

    contarletraa = cadena.count('a')

    repeticiones1 = longitud // len(cadena)
    areps = repeticiones1 * contarletraa

    residuo = longitud % len(cadena) #Indexea residuo
    numenresiduo = cadena[:residuo].count('a')

    afinal = areps + numenresiduo

    return afinal


cadena = input("Escribe string: ")
longitud = (input("Esscribe longitud:"))
longitud = int(longitud)

resultado = contarcadena(cadena, longitud)
print(resultado)





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