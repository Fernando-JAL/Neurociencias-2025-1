#. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def fibonacci(n):
    if n <= 0:
        raise ValueError("El número debe ser positivo y mayor que 0.")
    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    try:
        n = int(input("¿Qué posición de fibonacci quieres conocer?:"))
        if n <= 0:
            raise ValueError("El número debe ser positivo y mayor que 0.")
        print(f"La posición {n}  de Fibonacci es: {fibonacci(n)}")
    except ValueError as e:
        print(f"Error: {e}")

# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def fibonacci(n):
    if n <= 0:
        raise ValueError("El número debe ser positivo.")
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

if __name__ == "__main__":
    try:
        n = int(input("¿Cuántas posiciones de fibonacci quieres conocer?: "))
        if n <= 0:
            raise ValueError("El número debe ser positivo.")

        fib_sequence = fibonacci(n)
        print(f"Los primeros {n} términos de la serie de Fibonacci son: {fib_sequence}")
    except ValueError as e:
        print(f"Error: {e}")