# Retorno de valores
# Para comunicarse con el exterior, las funciones pueden devolver valores
# al proceso principal gracias a la instrucción return.
#
# En el momento de devolver un valor, la ejecución de la función finalizará:

def test():
    return [1,2,3,4,5]

# variable = test()
# print(variable)
#
# print('usando slicing:', variable[-2:])
# print('usando slicing:', test()[-2:])

# Envío de valores
# Para comunicarse con el exterior, las funciones no sólo pueden devolver valores,
# también pueden recibir información:

# Parámetros y argumentos
# En la definición de una función, los valores que se reciben se denominan parámetros,
# y en la llamada se denominan argumentos.

# def <nombre_de_funcion>(parametros):
#     #codigo
# nombre_de_funcion(argumentos)

# def test_funcion(parametro1, parametro2):
#     print(parametro1, parametro2)
#     return parametro1 + parametro2
#
# argumento1, argumento2 = 5, 12.5
# test_funcion(argumento1, argumento2)

def test_funcion(parametro1: int, parametro2: float) -> float:
    print(parametro1, parametro2)
    return parametro1 + parametro2

argumento1, argumento2 = 5, -12.85
# test_funcion(argumento1, argumento2)


# Trabajando con argumentos y parámetros
# Argumentos por posición
# Argumentos por nombre
def funcion1(a, b):
    print(a-b)

x, y = 25, 7
# funcion1(b = x, a = y)

# TypeError: funcion1() takes 2 positional arguments but 3 were given
# funcion1(-85, 7, [53])



# Parámetros por defecto
# Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros,
# y de ésa forma podríamos hacer una comprobación antes de ejecutar
# el código de la función:

def funcion_resta(a = 25, b = 7):
    print(a-b)

funcion_resta(a = 50, b = 10)