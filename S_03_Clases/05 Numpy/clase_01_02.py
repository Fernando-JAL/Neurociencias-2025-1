# Arrays pregenerados
# Crear arrays a partir de listas puede ser muy tedioso,
# por eso numpy integra varias funciones muy útiles para generar arrays de
# uso común en el álgebra de matrices.
#
# ARRAY DE CEROS
# Un array de ceros es cuando todos sus elementos son ceros.
# Podemos generarlos con el método zeros:
import numpy as np

array_0s = np.zeros(3)
print(array_0s)

arrau_0s_2d = np.zeros([2, 4])
print(arrau_0s_2d)


arrau_0s_3d = np.zeros([2, 2, 2])
print(arrau_0s_3d)
print('dimension de arrau_0s_3d', arrau_0s_3d.ndim)

# ARRAY DE UNOS
# Lo mismo podemos hacer pero utilizando el método ones:
array_1s = np.ones(6)
print(array_1s)

array_1s_2d = np.ones([3, 6])
print(array_1s_2d)

# Array de identidad
# Los arrays de identidad son matrices cuadradas (con el mismo número de
# filas que de columnas) donde todos los valores son ceros a excepción de la
# diagonal donde son unos. Podemos generarlos con el método eye:

array_id = np.eye(4)
print(array_id)

# Array de rangos
# Por último pero no por ello menos importante también es posible generar
# arrays a partir de un rango de valores. Para hacerlo utilizaríamos el
# método arange:

rango_range = np.arange(5)
print(rango_range)

rango_range = np.arange(-10, 50, 2) # formato = inicio, final, step
print(rango_range)



