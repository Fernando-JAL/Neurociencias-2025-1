"""
2) Realiza un programa que sume todos los números enteros pares desde el 0 hasta
un número que se introduzca por teclado

Sugerencia: Puedes utilizar la funciones sum() y range() para hacerlo más fácil.
El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números,
pruébalo.
"""

numero_str = input('Introduce un número: ')

numero = int(numero_str)
pares = range(0, numero+1, 2)
print('La suma de los pares hasta el número', numero, ' es: ', sum(pares))
