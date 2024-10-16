import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

###                    E X A M E N   2   M O D E L O S   C O M P U T A C I O N A L E S                    ###

# 0) Antes del Examen

## Cargar el Archivo
MentalHealth = pd.read_csv('MentalHealth4.csv')

## Comprobar que se cargó bien
print(MentalHealth.head())

filas, columnas = MentalHealth.shape
print(f"El CSV tiene {filas} filas y {columnas} columnas.")
#_________________________________________________________________________________________
# 1) Crear una función llamada "df_ordered" que reciba un dataframe y un str y
# retorne un dataframe ordenado de mayor a menor considerando la característica str

## --> Ordenar de mayor a menor, por país, según la prevalencia de Dysthymia

def df_ordered(dataframe, columna):
    df_ordenado = dataframe.sort_values(by=columna, ascending=False)
    return df_ordenado

columna_orden = 'Dysthymia'
df_ordenado = df_ordered(MentalHealth, columna_orden)

# Imprimir únicamente para las columnas 'Entity' y 'Dysthymia'
print('\nEjercicio 2')
print(df_ordenado[['Entity', 'Dysthymia']])

#_______________________________________________________________________________________
# 2) Crear una función llamada "plot_bar" que reciba un dataframe y un str y haga el plot de barras de ese
# dataframe considerando esa caracterísitca descrita por el string

def plot_bar(dataframe, columna):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Entity', y=columna, data=dataframe)
    plt.xticks(rotation=90)
    plt.title(f'Prevalencia de {columna} por País')
    plt.xlabel('País')
    plt.ylabel('Prevalencia')
    plt.tight_layout()
    plt.show()

plot_bar(df_ordenado, 'Dysthymia')

#___________________________________________________________________________________________
# 3) Países con mayor depresión

df_orden_depre = MentalHealth.sort_values(by='Major depression', ascending=False)

print('\nEjercicio 3')
print(df_orden_depre[['Entity', 'Major depression']])

#______________________________________________________________________________________________
# 4) Gráfica de barras mostrando el valor de depresión y la entidad (país)

df_ordenado_major_depression = MentalHealth.sort_values(by='Major depression', ascending=False)

plot_bar(df_ordenado_major_depression, 'Major depression')
#________________________________________________________________________________________________
# 5) Países con mayor desorden alimenticio

df_orden_eat = MentalHealth.sort_values(by = "Eating disorders", ascending= False)

print('\nEjercicio 5')
print(df_orden_eat[['Entity', 'Eating disorders' ]])
#_________________________________________________________________________________________________
# 6) Gráfica de barras mostrando el valor de desorden alimenticio y la entidad (país)

plot_bar(df_orden_eat, 'Eating disorders')
#__________________________________________________________________________________________________
# 7) Países con mayor Esquizofrenia
columna_orden_esqz = 'Schizophrenia'

df_ord_esqz = df_ordered(MentalHealth, columna_orden_esqz)

print('\nEjercicio 7')
print(df_ord_esqz[['Entity', 'Schizophrenia']])
#__________________________________________________________________________________________________
# 8) Gráfica de barras mostrando el valor de esquizofrenia y la entidad (país)

plot_bar(df_ord_esqz, 'Schizophrenia')
#___________________________________________________________________________________________________
# 9) Crear un data frame con los valores por país de ["Entity Code", "Year", "Schizophrenia disorders",
# "Depressive disorders", "Anxiety disorders", "Bipolar disorders", "Eating disorders"]

columnas_new = ["Entity", "Code", "Year", "Schizophrenia", "Major depression", "Anxiety disorders", "Bipolar disorder",
                "Eating disorders", "Dysthymia"]

new_MH = MentalHealth[columnas_new]
new_MH_ord = new_MH.sort_values(by='Entity')

columnas_numericas = ["Schizophrenia", "Year", "Major depression", "Anxiety disorders",
                      "Bipolar disorder", "Eating disorders", "Dysthymia"]

new_MH_ord[columnas_numericas] = new_MH_ord[columnas_numericas].apply(pd.to_numeric, errors='coerce')

print('\nEjercicio 9:')
print(new_MH_ord)
#_____________________________________________________________________________________________________
# 10) Mostrar los estadísticos del dataframe anterior. Min, max, valores nulos, media, cuartiles, desv estándar.

print('\nEjercicio 10:')

## Media, cuartiles, mínimo, máximo, desviación estándar
print("Estadísticos generales:\n")
print(new_MH_ord.describe())

## Cantidad de valores nulos por columna
print("\nValores nulos por columna:\n")
print(new_MH_ord.isnull().sum())

## Valor mínimo de las columnas numéricas
print("\nValores mínimos por columna numérica:\n")
print(new_MH_ord[columnas_numericas].min())

## Valor máximo de las columnas numéricas
print("\nValores máximos por columna numérica:\n")
print(new_MH_ord[columnas_numericas].max())
#__________________________________________________________________________________________________
# 11) Mostrar la distribución de cada feature del dataframe anterior

col_num_11 = ["Schizophrenia", "Major depression", "Anxiety disorders",
                      "Bipolar disorder", "Eating disorders", "Dysthymia"]

plt.figure(figsize=(15, 10))

for i, columna in enumerate(col_num_11, start=1):
    plt.subplot(3, 3, i)
    sns.histplot(new_MH_ord[columna], kde=True, stat='density', bins=30)
    plt.title(f'Distribución de {columna}')
    plt.xlabel(columna)
    plt.ylabel('Densidad')

plt.tight_layout()
plt.show()
#_________________________________________________________________________________________________
# 12) Mostrar en un mapa de color la correlación entre las features
# ["Schizophrenia", "Major depression", "Anxiety disorders", "Bipolar disorder", "Eating disorders"]

columnas_e12 = ["Schizophrenia", "Major depression", "Anxiety disorders", "Bipolar disorder", "Eating disorders"]
correlation_matrix = new_MH_ord[columnas_e12].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, cbar_kws={"shrink": .8})

plt.title('Mapa de Calor de la Correlación entre Trastornos de Salud Mental')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.tight_layout()

plt.show()

#_____________________________________________________________________________________________________
#-----------------------------------------------------------------------------------------------------
#_____________________________________________________________________________________________________

                                            # PARTE 2 DEL EXAMEN

data = pd.read_csv('cancer_reg.csv')

# 1) Mostrar la correlación entre las features [ 'target_deathrate', 'avganncount', 'avgdeathsperyear',
# 'incidencerate', 'medincome', 'povertypercent', 'pctprivatecoverage', 'pctpubliccoverage' ]

features = [
    'target_deathrate',
    'avganncount',
    'avgdeathsperyear',
    'incidencerate',
    'medincome',
    'povertypercent',
    'pctprivatecoverage',
    'pctpubliccoverage'
]
data_subset = data[features]

## Matriz de correlación
correlation_matrix = data_subset.corr()

print('Matriz de Correlación')
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()
#_________________________________________________________________________________________________
# 2) Mostrar la distribución de cada feature del dataframe anterior

plt.figure(figsize=(15, 10))

for i, feature in enumerate(features):
    plt.subplot(3, 3, i + 1)  # Ajusta el número de filas y columnas según sea necesario
    sns.histplot(data_subset[feature], kde=True, bins=30)  # Histograma con KDE
    plt.title(f'Distribución de {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()

#__________________________________________________________________________________________________
# 3) Aquellos que dependencia lineal encontrar los valores de la recta. hint: scipy

correlation_pairs = []

threshold = 0.7

for i in range(len(features)):
    for j in range(i + 1, len(features)):
        feature_x = features[i]
        feature_y = features[j]


        correlation = data_subset[feature_x].corr(data_subset[feature_y])


        if abs(correlation) > threshold:
            correlation_pairs.append((feature_x, feature_y))

            x = data_subset[feature_x]
            y = data_subset[feature_y]

            m, b = np.polyfit(x, y, 1)

            print(f'Dependencia lineal entre {feature_x} y {feature_y}:')
            print(f'  Pendiente (m): {m}')
            print(f'  Intercepto (b): {b}')
            print(f'  Correlación: {correlation}\n')

            plt.figure(figsize=(10, 6))
            plt.scatter(x, y, label='Datos', alpha=0.6)
            plt.plot(x, m * x + b, color='red', label='Línea de Regresión')
            plt.title(f'Regresión lineal entre {feature_x} y {feature_y}')
            plt.xlabel(feature_x)
            plt.ylabel(feature_y)
            plt.legend()
            plt.show()

print("Features con correlación lineal:")
for pair in correlation_pairs:
    print(f' - {pair[0]} y {pair[1]}')