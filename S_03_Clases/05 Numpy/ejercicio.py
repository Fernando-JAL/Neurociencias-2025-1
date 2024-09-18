import numpy as np

arr_2d = np.zeros((5,10))

for i,fila in enumerate(arr_2d):
    for j,columna in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j

# Ejercicio 1. Determine dimensión y forma de la matriz arr_2d
# Ejercicio 2. Transponga la matriz
# Ejercicio 3. Modifique los valores de la 5 columna por 999
# Ejercicio 4. Modifique los valores de las filas 3 y 4 por -5