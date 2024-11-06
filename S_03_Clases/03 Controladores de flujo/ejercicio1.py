# Ejercicio
"""
2) Recibe por teclado un número entero  𝑛  e imprime '123...n'

Ejemplo:

𝑛=5
  devuelve '12345'

Restricciones:

1≤𝑛≤150
"""
numero_str = input('Introduce un número del 1 al 150: ')
n = int(numero_str)

print(list(range(1, n+1)))


