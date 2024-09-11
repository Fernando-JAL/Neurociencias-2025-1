# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def ser_fibona (n):
# nombre_funcion->ser_fibona (serie de fibonacci)
# n -> la ocupo para saber al final la n-esima posicion

  if n <= 0: #n (int) es el que yo voy a ingresar;  n menor igual a 0
    return 0 #lo que me devuelve
  else:
    a, b = 0, 1 #ahora bien si n es mayor que 0 se retoman dos var
    #a->0 1er term
    #b->1 2doter
    for n in range(2, n+1): #iterando inicio de bucle
      a, b = b, a+b
    return b #fin bucle-> contiene el valor de la n-esima posicion

n = int(input("Hola soy Zaira, te solicitare que me indiques un valor para n: ")) # Reciba un entero


devuelve = ser_fibona(n)
print("Calculando para", n, "en la sucesión de Fibonacci la posicion n-esima es:", devuelve) # Devuelva el n-ésimo término de la serie de Fibonacci

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024


# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ
def ser_fibona(n):

  if n <= 0: #n menoor o igual a 0
    return [] #lista
  else: #cuando sea mayor n que 1
    seq_fibona = [0, 1]
    for n in range(2, n):
      seq_fibona.append(seq_fibona[-1] + seq_fibona[-2])
    return seq_fibona

n = int(input("Podrias teclear la cant. de números de términos que quieres saber de la sucesión de Fibonacci: "))
#aqui indico lo que quiero que el profe ingrese

devuelve = ser_fibona(n) #devuelve-> almacena el valor n +calculo
print("Para los ", n, "términos en la sucesión de Fibonacci deberian ser:", devuelve)
#imprimir el resultado final almacenado en devuelve

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024

# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. SherloCK debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

def cuadrados_rango(a, b):
  #considero a y b para la representar super e infer

  c_cuadrados = 0 #  c_cuadrados es a debo contar cuantoss cuadrados perfect llevo encontrados
  i = 1 #i mi var que tiene la func de contar y generar numeros
  cuadrado = 1 #almaceno valor del cuadrado

  while cuadrado <= b: #inicio bucle cuando sea menor o igual de b
    if a <= cuadrado <= b: #si esta dentro del rango a y b
      c_cuadrados += 1
    i += 1 #se incrementa val i y paso al int
    cuadrado = i * i #calcular el cuadrado del val nuevo
  return c_cuadrados, i #val final
a = int(input("El primer paso es que escribas el límite inferior del rango: "))

b = int(input("El segundo psso es que escribas el límite superior del rango: "))

devuelve = cuadrados_rango(a, b)
print("Finalmente , obtenemos que hay", devuelve, "cuadrados perfectos dentro del rango de", a, "a", b)

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024


# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

def cont_a(s, n):
    #func->cont_a : s-> string & n-> cant_letras en cadena
    tam_s = len(s) # Calcular tamaño de la cadena s guardar en tam_s
    rep_t= n // tam_s # para saber cuanto cabe en la cadena 's' en las primeras letras
    resto = n % tam_s #de la div anterior


    cont_t = s.count('a') * rep_t # cantidad total de 'a' en las partes repetidas de la cadena

    cont_t += s[:resto].count('a') #Suma al contador anterior

    return cont_t #devuelve el valor final del contador,


# en la cadena y el número de letras
s = input("Escribe la cadena por ejemplo 'abcabc': ")
n = int(input("Agrega el número de letras por ejemplo '10': "))

# para calcular e imprimir
resultado = cont_a(s, n)
print("Aqui tenemos que ", resultado, "letras 'a' en las primeras", n, "letras.")

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024


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

def cort_bast(longitudes):

  resultado = []
  while longitudes:
    resultado.append(len(longitudes))
    minimo = min(longitudes)