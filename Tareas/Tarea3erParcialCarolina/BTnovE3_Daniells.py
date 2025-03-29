import scipy.io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

                                            ### EJERCICIO 3 ###

# E3 Parte 1: Generar un número aleatorio entero en el rango [-3, 3] con seed=5002
seed_value = 5002
np.random.seed(seed_value)

randnum1 = np.random.randint(-3, 4)
print("Primer número aleatorio:", randnum1)

# E3 Parte 2: Generar un número aleatorio flotante en el rango [-10, 10] con seed=5002
np.random.seed(seed_value)

randfloat2 = np.random.uniform(-10, 11)
print("Número flotante aleatorio:", randfloat2)

# E3 Parte 3: Genera un array de 1000 números con distribución normal, con mu= ej1, y sigma= ej2
normal_array = np.random.normal(loc=randnum1, scale=randfloat2, size=1000)

df = pd.DataFrame(normal_array, columns=['Distribución Normal'])

print(df.head())

# E3 Parte 4: Plotear la distribución de los 1000 números
plt.figure(figsize=(10, 6))

plt.hist(normal_array, bins=30, color='skyblue', edgecolor='black')

plt.title('Distribución Normal del array de 1000 números')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

# E3 Parte 5: Calcular el valor de 1sigma, 2sigma, 3sigma
media = randnum1
sigma = randfloat2

rango_1_sigma = (media - sigma, media + sigma)
rango_2_sigma = (media - 2 * sigma, media + 2 * sigma)
rango_3_sigma = (media - 3 * sigma, media + 3 * sigma)

print("Rango para 1 desviación estándar (68%):", rango_1_sigma)
print("Rango para 2 desviaciones estándar (95%):", rango_2_sigma)
print("Rango para 3 desviaciones estándar (99.7%):", rango_3_sigma)

#E3 Parte 6: Calcular el porcentaje de números que están en el rango [-1sigma, 1sigma], [-2sigma, 2sigma],
# [-3sigma, 3sigma]

total_datos = len(normal_array)

en_1_sigma = np.sum((normal_array >= (media - sigma)) & (normal_array <= (media + sigma)))
en_2_sigma = np.sum((normal_array >= (media - 2 * sigma)) & (normal_array <= (media + 2 * sigma)))
en_3_sigma = np.sum((normal_array >= (media - 3 * sigma)) & (normal_array <= (media + 3 * sigma)))

porcentaje_1_sigma = (en_1_sigma / total_datos) * 100
porcentaje_2_sigma = (en_2_sigma / total_datos) * 100
porcentaje_3_sigma = (en_3_sigma / total_datos) * 100

print(f"Porcentaje de números en el rango [-1σ, 1σ]: {porcentaje_1_sigma:.2f}%")
print(f"Porcentaje de números en el rango [-2σ, 2σ]: {porcentaje_2_sigma:.2f}%")
print(f"Porcentaje de números en el rango [-3σ, 3σ]: {porcentaje_3_sigma:.2f}%")

print('\n CAMBIO')

# E3 Parte 7: Función masiva
def analizar_distribucion_normal(mu, sigma, total_numeros):
    normal_array = np.random.normal(loc=mu, scale=sigma, size=total_numeros)

    plt.figure(figsize=(10, 6))
    plt.hist(normal_array, bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribución Normal')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

    rango_1_sigma = (mu - sigma, mu + sigma)
    rango_2_sigma = (mu - 2 * sigma, mu + 2 * sigma)
    rango_3_sigma = (mu - 3 * sigma, mu + 3 * sigma)

    en_1_sigma = np.sum((normal_array >= rango_1_sigma[0]) & (normal_array <= rango_1_sigma[1]))
    en_2_sigma = np.sum((normal_array >= rango_2_sigma[0]) & (normal_array <= rango_2_sigma[1]))
    en_3_sigma = np.sum((normal_array >= rango_3_sigma[0]) & (normal_array <= rango_3_sigma[1]))

    porcentaje_1_sigma = (en_1_sigma / total_numeros) * 100
    porcentaje_2_sigma = (en_2_sigma / total_numeros) * 100
    porcentaje_3_sigma = (en_3_sigma / total_numeros) * 100

    print(f"Rango de 1 sigma ({rango_1_sigma}): {porcentaje_1_sigma:.2f}% de los datos")
    print(f"Rango de 2 sigma ({rango_2_sigma}): {porcentaje_2_sigma:.2f}% de los datos")
    print(f"Rango de 3 sigma ({rango_3_sigma}): {porcentaje_3_sigma:.2f}% de los datos")


# E3 Parte 8: Usar la función anterior con los valores (0, 1., 1000), (3, 5, 5000), (-3, 3, 10000)
print('ejemplo 1:', analizar_distribucion_normal(mu=0, sigma=1, total_numeros=1000))
print('ejemplo 2:', analizar_distribucion_normal(mu=3, sigma=5, total_numeros=5000))
print('ejemplo 3:', analizar_distribucion_normal(mu=-3, sigma=3, total_numeros=10000))

