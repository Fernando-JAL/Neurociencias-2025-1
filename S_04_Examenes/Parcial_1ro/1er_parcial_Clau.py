# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
# $F(n) = F(n-1) + F(n-2)$ donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros
# términos son: $F(1) = 1$ y $F(2) = 1$.
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ
n = int(input("Coloca un no.")) # solicitar que ingrese no.
def fibonacci(n): # establecer función
    if n <= 0:
        return "El no. debe ser positivo -_- " # para que admita entrada
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # ecuación fibonacci

print("El n-ésimo término es: ", fibonacci(n)) # imprimir código

## fail
#n = int(input("Coloca un no."))
#def fibonacci(n): # establecer función
#    return fibonacci(n - 1) + fibonacci(n - 2)  # ecuación fibonacci



# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos
# términos de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ
for i in range(1, n+1): # Utilizar: for y range (inicio, fin)
    print("Los primeros términos son:", fibonacci(i)) # imprimir primeros términos llamando la función fibonacci



# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final
# que describa el rango de enteros. Sherlock debe determinar el número de cuadrados enteros dentro del rango.
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número de cuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ
a = int(input("Dame el valor inicial del rango, Watson:"))
b = int(input("Dame el valor final del rango, Watson:"))

import math # ayuda de math
def cuad_ent (a,b): # establecer función
    r_a = math.ceil(math.sqrt(a)) # 1° entero, raíz >=a
    r_b = math.floor(math.sqrt(b)) # 2° entero, raíz <=b
    return max(r_b - r_a)

answ = cuad_ent(a, b) # esta es la respuesta
print("Ok, el no. de cuadrados es:", answ) # imprimir

## Otro fail...
#a = int(input("Dame el valor inicial del rango, Watson:"))
#b = int(input("Dame el valor final del rango, Watson:"))
#def cuad_ent (a,b): # establecer función
#    r_a = sqrt(a) and >=a # 1° entero, raíz >=a...?
#    r_b = sqrt(b) and <=b # 2° entero, raíz <=b???
#    return (r_b - r_a)
#answ = cuad_ent(a, b) # esta es la respuesta
# print("Ok, el no. de cuadrados es:", answ) # imprimir



# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e imprime el
# número de letras 'a' en las primeras $n$ letras de la cadena infinita.
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras
# $n$ letras de la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ
s = str(input("Ingresa la cadena en minúsculas:")) # solicitar al usuario
n = int(input("Ingresa el no. de letras:"))

def con_cad(cadena, n): # definir función
    lon_cad = len(cadena) # longitud cadena
    cad_a = cadena.count('a') # contar "a"s
    rep_cad = n // lon_cad # repetición completa?
    cad_rest = n % lon_cad # letras restantes
    cont_add = cadena[:cad_a].count('a')
    return rep_cad * cad_a + cont_add # retornar as

resp = con_cad(s, n)
print('El no. de "a"s es:', resp)



# 5. Dada una lista de enteros que representan las longitudes de bastones, debes iterativamente cortar los bastones en
# bastones más cortos descartando las piezas más cortas hasta que no queden ninguna. En cada iteración debes determinar
# la longitud del bastón más corto. Cuando los bastones remanentes son de la misma longitud, no pueden ser recortados
# más entonces se descartan.
# - Crear una función que reciba una lista de enteros, y retorne el número de bastones en cada iteración
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
# def cont_bas (long): # definir función
#    while long:
#        long. append(len(long))
#        long = [x in long if long > 0]
#    return res
## pass