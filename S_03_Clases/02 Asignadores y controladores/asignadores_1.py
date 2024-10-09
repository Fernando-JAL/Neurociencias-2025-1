# Asignadores
#Operadores de asignación, relacionales y lógicos
# En programación, una variable está formada por un espacio en el
# sistema de almacenaje y un nombre simbólico que está asociado a dicho espacio.

#Ese espacio contiene una cantidad de información conocida o desconocida, es decir un valor.

variable1 = tuple('-78.3214568542', )
variable2 = (2, 4, 6)

# Operadores de asignación
# Los operadores de asignación que se verán en el curso son:
# =, +=, -=, *=, /=, //= %= **=
variable1 = 5
print('La variable1 = ', variable1)

variable1 += 3.2
#variable1 = variable1 + 3.2
print('La variable1 = ', variable1)

variable1 -= 17.2
#variable1 = variable1 - 17.2
print('La variable1 = ', variable1)

# Ejemplo con **=
variable1 = 2
variable1 **=3
print('Usando **=. La variable1 = ', variable1)

# Aplicando suma a cadenas
cad1 = 'hola'
cad2 = ' que hace'
print(cad1 + cad2)

cad1 += cad2
print(cad1)

# Operadores relacionales
# Los operadores relacionales a considerar son:
# <, >, ==, !=

# Operadores lógicos
# Los operadores lógicos son or, and y not
#
# not - es la negación lógica

# Expresiones anidadas
# Se pueden solucionar empleando las reglas de precedencia:
#
# Primero los paréntesis porque tienen prioridad
# Segundo, las expresiones aritméticas por sus propias reglas
# Tercero, las expresiones relacionales
# Cuarto, las expresiones lógicas

