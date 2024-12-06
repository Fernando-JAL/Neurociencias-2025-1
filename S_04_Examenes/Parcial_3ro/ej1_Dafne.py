# Ejercicio 1
def lanzamiento(n: int) -> float:

    # Total de posibles combinaciones con dos dados de 6 caras
    total_combinaciones = 6 * 6

    # Combinaciones válidas donde la suma de los dados <= n
    combinaciones_validas = 0
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 <= n:
                combinaciones_validas += 1

    # Cálculo de la probabilidad
    probabilidad = combinaciones_validas / total_combinaciones
    return probabilidad

# Prueba de la función
lanzamiento(5)  # n = 5





