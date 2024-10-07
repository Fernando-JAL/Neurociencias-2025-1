import pandas as pd

# Preguntar cuántas columnas tendrá el DataFrame
num_columnas = int(input("Pon acá el número de columnas que tendrá el DataFrame --> "))

# Creando lista para almacenar los datos de cada columna
datos = []

# Preguntar los datos de cada columna
for i in range(num_columnas):
    columna = input(f"Escribe los datos de la columna {i+1} (separar con comas): ").split(',')
    datos.append(columna)

# Preguntar los nombres de las columnas
nombres_columnas = input("Escribe los nombres de las columnas (separar coon comas): ").split(',')

# Preguntar los nombres de las filas
nombres_filas = input("Escribe los nombres de las filas (separar con comas): ").split(',')

# Creando el DataFrame
df = pd.DataFrame(data=dict(zip(nombres_columnas, datos)), index=nombres_filas)

# Mostrando el DataFrame
print("\n Mi DataFrame:")
print(df)
