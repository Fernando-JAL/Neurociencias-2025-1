# Las funciones
# Son fragmentos de código que se pueden ejecutar múltiples veces.
# Pueden recibir y devolver información para comunicarse con el proceso principal.
#
# Definición y llamada
def saludar():
    print("Hola! Este print se llama desde la función saludar()")

# saludar()

def escribir_tabla_del_5():
    for i in range(10):
        print('5 * ', i+1, ' = ', 5*(i+1))

# escribir_tabla_del_5()

# formas de usar el print
val = 10
# print('5 *', val, '=', 5*val)
# print('5 * {} = {}'.format(10, 50))
# print('5 * {1} = {0}'.format(10, 50))
# print('5 * {0} = {1}'.format(10, 50))
# print(f'5 * {val} = {5*val}')


# Variables globales vs variables locales
# Una variable declarada en una función no existe en la función principal:
def test():
    n = 10
    print(n)

def test1():
    n = 20
    print(n)

# print('antes de las funciones')
# test()
# print('después de la función test pero antes de test1')
# test1()
# print('después de test1')

# return en las funciones

def test_con_return():
    n = 10
    print('localmente n = ', n)
    return n*5

# m = test_con_return()
# print('globalmente m = ', m)


def test_con_multiple_return():
    n = 10
    print('localmente n = ', n)
    return n, n*5, 6**2, [5, 'lobo']

# vals = test_con_multiple_return()
# print(vals, type(vals))
#
# val1, val2, val3, val4 = test_con_multiple_return()
# print('vals:', val1, val2, val3, val4)


# Aplicación de global dentro de una función
def test_funcion():
    global variable
    variable = 10 #variable local
    print(variable)

variable = 20 #variable global
print(variable)
test_funcion()
print(variable)





