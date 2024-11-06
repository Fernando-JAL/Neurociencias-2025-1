# 1er examen Anel Mendiola

# EJERCICIO 1.
## Función de Fibonacci : 1, 1, 2, 3, 5 ,8 ,13, 21, 34, 55

# x = int(input("Ingresa un número positivo: "))
# # pedimos que ingrese un valor
#
# def funcion1 (x):
#     if x == 1 or x ==1:
#         return 1
#     else:
#         valor1, valor2 = 1,1
#         for _ in range(x-2):
#             valor1, valor2 = valor2, valor1+valor2
#     return valor2
#
# print(f"El valor {x} de la serie de Fibonacci es: ", funcion1(x))

## creo que sí salió !!!!! -> si pones 4, el cuarto valor de la función es 3
## espero sea así, si no, ya ni modo

# EJERCICIO 2
# x = int(input("Ingresa un número entero: "))
# # pedimos que ingrese un valor y que se lea como entero

# def funcion2 (x):
#     serie = [ ] #aquí queremos meter los datos que ingrese el usuario, no?
#     valor1, valor2 = 1, 1
#     for i in range(x):
#         if i == 0:
#             serie.append(valor1)
#         elif i == 1:
#             serie.append(valor2)
#         else:
#             valor1, valor2 = valor2, valor1+valor2
#             serie.append(valor2)
#     return serie
#
# print(f"Los valores {x} de la serie son: {funcion2(x)}")
## eeeeee omg siiiiiii salió

# EJERCICIO 3
import math

valor_inicial = int(input("Dame un valor inicial: "))
valor_final = int(input("Dame un valor final: "))

def enteros(n1, n2):
    inicio = math.sqrt(n1)
    final = math.sqrt(n2)
    if inicio > final:
        return 0  # queremos que los valores queden dentro del rango
    else:
        return final - inicio + 1

print(f"El numero de cuadrados enteros en el rango obtenido es: {enteros(n1, n2)}")
#### el ejercicio no quiso correr no sé por qué
### decía que la función n1 y n2 no estaban definidas, pero según yo, si deberían salir
### AYUDAAAAAAA

# EJERCICIO 4

a = input("ingresa una serie de letras en minusculas que incluya la letra a : ")
n = int(input("Ingresa un número entero: "))

# ay no entiendo, ya me voy :(