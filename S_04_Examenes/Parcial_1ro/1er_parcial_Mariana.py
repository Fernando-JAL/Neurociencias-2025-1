# Ejercicip 1
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(int("Introduce un número entero"))
print('Término de la serie', fibonacci())



#Ejercicio 2


#Ejercicio 3
def cuenta_rango(a, b):
    cuenta = 0
    n = 1
    while n*n <=b:
        if n*n >= a:
            cuenta += 1
        n+= 1
        return cuenta

a= 6
b= 60
print ('Números con cuadrados',cuenta_rango(a,b))

#Ejercicio 4
def contar_as(s, n):
    repeticiones = (n + len(s) - 1) // len(s)
    cadena_repetida = s * repeticiones
    total_as = cadena_repetida[:n].count('a')
    return total_as


s = input("Ingrese palabra s: ")
n = int(input("Ingrese  número n: "))

resultado = contar_as(s, n)
print(f"Número de letras 'a' en las primeras {n} letras de la cadena: {resultado}")

#Ejercicio 5
def cortar(bastones):
        salida = []
        while bastones:
            salida.append(len(bastones))
            min_longitud = min(bastones)
            bastones = [bastón - min_longitud for bastón in bastones if bastón > min_longitud]
        return salida

bastones = [5, 4, 4, 2, 2, 8]
print(cortar(bastones))