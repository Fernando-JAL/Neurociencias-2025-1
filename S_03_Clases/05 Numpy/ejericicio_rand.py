import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd

# Generar números aleatorios con distribución normal (0, 1)
# array uniforme con curva gaussiana
arreglo = np.random.normal(size=1000000)
print(f'media = {np.mean(arreglo)}, std = {np.std(arreglo)}')
plt.hist(arreglo, bins=100)
plt.show()

# Ejercicio. Transformar los datos con distribución normal (0, 1) a
# distribución normal (5, 2)
mu, sigma = 5, 4
arreglo = arreglo * sigma + mu

plt.hist(arreglo, bins=100)
print(f'media = {np.mean(arreglo)}, std = {np.std(arreglo)}')
plt.show()