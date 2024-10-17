# Paso por valor y paso por referencia
# Paso por valor: Se crea una copia local de la variable dentro de la función.
# Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro le afectarán también fuera.
# Tradicionalmente, los tipos simples se pasan automáticamente por valor y los compuestos por referencia.
#
# Simples: Enteros, flotantes, cadenas, lógicos...
# Compuestos: Listas, diccionarios, conjuntos...
# Ejemplo paso por valor


def duplicar_numero(numero):
    print('en la función: ', numero*2)

val = 10
print('antes de la función:', val)
duplicar_numero(val)
print('después de la función', val)



def duplicar_valores_lista(lista):
    for i, n in enumerate(lista):
        lista[i] *= 2 # lista[i] = lista[i] * 2
    print('dentro de la función', lista)

ns = [10, 50, 100]
print('antes de la función:', ns)
duplicar_valores_lista(ns[:])
print('después de la función', ns)
