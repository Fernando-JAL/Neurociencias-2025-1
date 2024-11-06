import numpy as np

arr_2d = np.zeros((5,10))

for i,fila in enumerate(arr_2d):
    for j,columna in enumerate(fila):
        arr_2d[i][j] = len(fila) * i + j

# Ejercicio 1. Determine dimensión y forma de la matriz arr_2d
print(f'dimensión = {arr_2d.ndim} y forma = {arr_2d.shape}')

# Ejercicio 2. Transponga la matriz
print('La transpuesta de la matriz es:\n', arr_2d.T)

# Ejercicio 3. Modifique los valores de la 5 columna por 999
arr_2d[:, 4] = 999
print('La matriz con la 5ta columna modificada es:\n', arr_2d)

# Ejercicio 4. Modifique los valores de las filas 3 y 4 por -5
arr_2d[2:4, :] = -5
print('La matriz con las filas 3 y 4 modificadas es:\n', arr_2d)

