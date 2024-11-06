# 1) Create a function that get an integer and calculate the factorial of
# that number (a non-negative integer)
def factorial(valor: int) -> int:
    if valor < 0:
        print('No existe el factorial de un número negativo')
        return

    resultado = 1
    for i in range(2, valor+1):
        resultado *= i

    return resultado

# val = float(input('Introduce un número entero para calcular el factorial: '))
# print(factorial(val))


# 2) Create a function that receives 3 numbers and verify if the third number is
# between the 2 first numbers
def verificacion_de_valor(val1, val2, val3):
    if val1 <= val3 <= val2:
        print('Si')
    else:
        print('No')

# valores_str = input('Introduce 3 valores: ')
# val1_str, val2_str, val3_str = valores_str.split()
# val1, val2, val3 = float(val1_str), float(val2_str), float(val3_str)

# val1, val2, val3 = list(map(float, input('Introduce 3 valores: ').split()))
# verificacion_de_valor(val1, val2, val3)


# 3) Given a string, create 2 functions to count the number of spaces in the string
def metodo1(palabra: str) -> int:
    numero_espacios = 0
    for letra in palabra:
        if letra == ' ':
            numero_espacios += 1
    return numero_espacios

def metodo2(palabra: str):
    numero_espacios = palabra.count(' ')
    print(f'La frase tiene {numero_espacios} espacios')

# cadena = input('introduce una frase: ')
# print(metodo2(cadena))


# 4) Given a list, create a function to print the odd numbers in the list
def imprimir_impares(lista: list):
    for numero in lista:
        if numero % 2 == 1:
            print(numero, end=' ')

listado = [2, 4, 2, 6, 23, 7, 3, 67, 23, 6]
imprimir_impares(listado)