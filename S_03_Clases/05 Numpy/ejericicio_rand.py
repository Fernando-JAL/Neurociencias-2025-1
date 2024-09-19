import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generar números aleatorios con distribución normal (0, 1)
# array uniforme con curva gaussiana
arreglo = np.random.normal(size=1000000)
# plt.hist(arreglo, bins=100)
# plt.show()

# Ejercicio. Transformar los datos con distribución normal (0, 1) a
# distribución normal (5, 2)
lista = []
mu, sigma = 5, 2
for valor in arreglo:
    nuevo_valor = valor * sigma + mu
    lista.append(nuevo_valor)

plt.hist(arreglo*sigma + mu, bins=100)
plt.show()