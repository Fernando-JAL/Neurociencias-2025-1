# Sentencia For (Para) con listas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for idx in numeros:  # Para [variable local] en [lista]
    # código para ser realizado en el fo
    print(idx)


# Ejemplo 2.
promedio = 0
numeros = [0, 2, 4, 5, 6, 8]
for idx in numeros:
    promedio += idx
    print(str(idx))
promedio /= len(numeros)
print('el promedio es: ', promedio)



#Ejemplo 3.
numeros = [0, 2, 4, 5, 6, 8]
diosito = 0
for var_local in numeros:
    diosito += 1
    print('se está ejecutando el for')
print('la longitud de la lista es: ', diosito)




# enumerate(iterable, start=0)¶
lista = ['azul', 'verde', 56, ['2da lista']]
print(list(enumerate(lista)))

for idx, elemento in enumerate(lista):
    print('indice:', idx, 'elemento:', elemento)

for idx, elemento in enumerate(lista):
    print(lista[idx])
# o equivalentemente
for elemento in lista:
    print(elemento)

# USO DE continue y break
for idx in range(2, 18):
    if idx > 16:
        continue
    print(idx)


for letra in 'palabra':
    print(letra)



