# Controladores de flujo
# Se trata de una estructura de control condicional.
# Nos permite evaluar si una o más condiciones se cumplen,
# para decir qué acción vamos a ejecutar.
# Esta evaluación de condiciones sólo puede dar un resultado Verdadero o un resultado Falso.

# Sentencia If (Si)
# Permite dividir el flujo de un programa en diferentes caminos.
# El if se ejecuta siempre que la expresión que comprueba devuelva True

var1, var2 = 5, 2
if True:
    print('caso positivo')
    if var2/var1 < var1:
        print('segundo nivel de if')

# Ejemplo de if else
condicional = (5 - 16) and False
if condicional:
    print('la condicional es verdadera')
else:
    print('la condicional es falsa')

# Ejemplo de if else
n = -9854105
if n % 2 == 0:
    print(n, "es un número par")
else:
    print(n, "es un número impar")

# Tercer comando elif
condicional = 32
if condicional < 10:
    print('condicional es chiquito')
elif condicional < 20:
    print('condiconal es grande')
else:
    print('no entró a ningún elif')

#equivalencia con if else
condicional = 32
if condicional < 10:
    print('condicional es chiquito')
else:
    if condicional < 20:
        print('condiconal es grande')
    else:
        print('no entró a ningún elif')

# Comando pass
if condicional != 0:
    pass
