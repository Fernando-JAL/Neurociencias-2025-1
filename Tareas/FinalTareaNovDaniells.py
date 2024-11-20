import scipy.io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

                       ##########     T A R E A     3 E R     P A R C I A L     ##########




                                             ### EJERCICIO 1 ###

# Parte 0: Preparando los archivos y datos
mat_path = r"C:\Users\dnlls\PycharmProjects\BrainToolbox\BCT\2019_03_03_BCT\data_and_demos\Coactivation_matrix.mat"
mat_json = scipy.io.loadmat(mat_path)

coactivation_matrix = mat_json['Coactivation_matrix']

matDict = {k:v for k, v in mat_json.items() if k[0] != '_'}
matDict.keys()

# E1 Parte 1: Dataframe con columnas e índices numerados desde 1
df = pd.DataFrame(coactivation_matrix, index=range(1, coactivation_matrix.shape[0] + 1),
                  columns=range(1, coactivation_matrix.shape[1] + 1))
print('Imprimiendo DataFrame con columnas e índices numerados desde 1:', df)

# E1 Parte 2: Heatmap de coactivation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(df, cmap='magma')
plt.title("Heatmap de Coactivation Matrix")
plt.show()

# E1 Parte 3: Subconjunto del dataframe de la fila 10 a la 30 y de la columna 10 a la 30
df_subset = df.loc[10:30, 10:30]

# E1 Parte 4: Mostrar el heatmap del subconjunto
plt.figure(figsize=(8, 6))
sns.heatmap(df_subset, cmap='magma')
plt.title("Heatmap del subconjunto (Filas 10-30, Columnas 10-30)")
plt.show()

# E1 Parte 5: Crear el grafo dirigido del subconjunto
G = nx.from_pandas_adjacency(df_subset, create_using=nx.DiGraph())

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=700, font_size=10, font_weight='bold', arrows=True, arrowstyle='-|>')
plt.title("Grafo dirigido del subconjunto (Filas 10-30, Columnas 10-30)")
plt.show()

# E1 Parte 6: Determinar el nodo con más conexiones en el nuevo dataset
max_connections_node = max(G.out_degree, key=lambda x: x[1])
print(f"El nodo con más conexiones en el subconjunto es: {max_connections_node[0]}, con {max_connections_node[1]} conexiones.")

# E1 Parte 7: Calcular los quantiles 0.25, 0.5 y 0.75 de la matriz de coactivación completa
cx =df.values.flatten()
print('Los cuantiles para el arreglo son:\n',pd.Series(cx).quantile([0.25,0.5,0.75]))

cx0= cx[cx!= 0]
quantiles = pd.Series(cx0).quantile([0.25, 0.5, 0.75])
print('cuantiles:\n', quantiles)

# E1 Parte 8: Mostrar el histograma de distribución de los valores de la matriz de coactivación
plt.figure(figsize=(10, 6))
plt.hist(quantiles, bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma de distribución de valores de la matriz de coactivación")
plt.xlabel("Valor de coactivación")
plt.ylabel("Frecuencia")
plt.show()

# E1 Parte 9: Binarizar la matriz de coactivación del subconjunto usando un threshold de 0
df_subset_binary = df_subset.map(lambda x: 1 if x > 0 else 0)
print("Parte 9. Matriz binarizada:\n", df_subset_binary)

plt.figure(figsize=(8, 6))
sns.heatmap(df_subset_binary, cmap='YlGnBu', cbar=False)
plt.title("Heatmap del subconjunto binarizado")
plt.show()



                                            ### EJERCICIO 2 ###

# E2 Parte 0: Preparando archivos y datos
fvemat = scipy.io.loadmat(r"C:\Users\dnlls\PycharmProjects\BrainToolbox\BCT\2019_03_03_BCT\data_and_demos\fve32.mat")

# E2 Parte 1: Muestra el heatmap de la matriz de activación
fvemat_dict= {k:v for k, v in fvemat.items()if k[0] != '_'}
plt.figure(figsize=(15, 10))
sns.heatmap(fvemat_dict['CIJ'],cmap='YlGnBu',vmax= 2)
plt.title('Heatmap de fve32.mat')
plt.show()

# E2 Parte 2: Utilizando los nombres del archivo .mat, muestra el grafo en 4 formas distintas
# (shell debe ser una de ellas)

framedate = pd.DataFrame(fvemat_dict['CIJ'], index= fvemat_dict['Names'], columns= fvemat_dict['Names'])
G = nx.Graph(framedate)
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title('fve32.map en estándar')
nx.draw_networkx(G, node_color='y', with_labels=True)
plt.show()

plt.subplot(2, 2, 2)
plt.title('fve32.map en Circular')
nx.draw_circular(G, node_color='r', with_labels=True)
plt.show()

plt.subplot(2, 2, 3)
plt.title('fve32.map en Shell')
Pform = nx.shell_layout(G)
nx.draw(G, Pform, with_labels=True)
plt.show()

plt.subplot(2, 2, 4)
plt.title('fve32.map en Kamada-Kawai')
Pformkamada = nx.kamada_kawai_layout(G)
nx.draw(G, Pformkamada, with_labels=True, node_color= 'olivedrab')
plt.show()

# E2 Parte 3: Determina el nodo con mayores conexiones
maxnode = max(G.degree, key=lambda x: x[1])
print(f"El nodo con más conexiones es {maxnode[0]}")

# E2 Parte 4: Muestra el grado solo destacando las conexiones del nodo encontrado en el ejercicio anterior
print(f"El nodo del ejercicio anterior, tiene un grado de: {maxnode[1]/2}")



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

