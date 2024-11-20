import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io
from matplotlib import animation


# EJERCICIO 1: Cree una funcion llamada 'lanzamiento' que reciba un entero llamado 'n' y retorne un flotante
# que calcule la probabilidad de que el lanzamiento de 2 dados de 6 caras sea <= n.



########## Parte 1: SIN IMPORTAR EL ORDEN DE LA COMBINACIÓN DE LOS DADOS ##########

def calcular_combinaciones_y_probabilidad(n):
    combs_validas = 0
    combs_total = 6 * 6

    for dado1 in range(1, 7):
        dado2 = n - dado1
        if 1 <= dado2 <= 6 and dado1 <= dado2:
            combs_validas += 1

    resultadofinaldado = combs_validas / combs_total

    return combs_validas, resultadofinaldado

n = int(input("Introduce el valor de 'n': "))
combinaciones, resultadofinaldado = calcular_combinaciones_y_probabilidad(n)
print(f"El número de combinaciones posibles para sumar {n} es: {combinaciones}")
print(f"El valor de resultadofinaldado es: {resultadofinaldado}")


########## Parte 2: CONSIDERANDO EL ORDEN DE COMBINACIÓN DE LOS DADOS ########

def calcular_combinaciones_y_probabilidad_con_orden(n):
    combs_validas = 0
    combs_total = 6 * 6

    for dado1 in range(1, 7):
        dado2 = n - dado1
        if 1 <= dado2 <= 6:
            combs_validas += 1

    resultadofinaldado = combs_validas / combs_total

    return combs_validas, resultadofinaldado

n = int(input("Introduce el valor de 'n'. Ahora consideraremos el orden: "))
combinaciones, resultadofinaldado = calcular_combinaciones_y_probabilidad_con_orden(n)
print(f"El número de combinaciones posibles para sumar {n} (considerando el orden) es: {combinaciones}")
print(f"El valor de resultadofinaldado es: {resultadofinaldado}")
