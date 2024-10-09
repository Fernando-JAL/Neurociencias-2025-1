# funciones de entrada y salida de datos

# función de entrada de datos: input()

string = input('Introduce un número:\n')

print('se recibió la cadena:', string)
print('con tipo de dato:', type(string))

numero = float(string)
print('el numero es:', numero, ' con tipo de dato: ', type(numero))
