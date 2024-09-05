# Funciones recursivas
# Se trata de funciones que se llaman a sí mismas durante su propia ejecución.
# Funcionan de forma similar a las iteraciones, y debemos encargarnos de planificar
# el momento en que una función recursiva deja de llamarse o tendremos una función
# rescursiva infinita.
#
# Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea
# más fácil abordar el problema y solucionarlo.
#
# Ejemplo sencillo sin retorno
# Cuenta regresiva hasta cero a partir de un número:
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)

cuenta_atras(5)


def quitando_letra(palabra):
    if len(palabra) > 0:
        print('palabra:', palabra)
        palabra = palabra[:-1]
        quitando_letra(palabra)
    else:
        print('palabra nula', palabra)
    print('saliendo de la funcion, ', len(palabra))

# quitando_letra('123')

def factorial(valor: int) -> int:
    if valor < 0:
        print('No existe el factorial de un número negativo')
        return
    resultado = 1
    for i in range(2, valor+1):
        resultado *= i
    return resultado

print('metodo clásico', factorial(8))

def factorial_recursivo(n):
    if n < 1:
        return 1
    return n * factorial_recursivo(n - 1)

print('metodo recursivo', factorial_recursivo(8))


