import funciones_1er_examen # paquete en la misma carpeta
import S_04_Examenes.Parcial_1er_solucion # paquete que está en otra carpeta
from funciones_1er_examen import cadena_infinita # uso de from
from funciones_1er_examen import fibonacci3 as fb # uso de from y as
from funciones_1er_examen import fibonacci, fibonacci2, cadena_infinita2

import paquetes.modulo_prueba as hola

print("Usando fibonaccio desde un modulo", funciones_1er_examen.fibonacci2(8))
print('Otra funcion del mismo modulo', funciones_1er_examen.cadena_infinita2('aba', 15))

print('funcion de otro modulo', S_04_Examenes.Parcial_1er_solucion.cuadrados_enteros2(3, 200))
print('uso de from', cadena_infinita('abacho', 22))
print('usando from para mandar llamar una funcion ', fb(6))
hola.saludo_func()
