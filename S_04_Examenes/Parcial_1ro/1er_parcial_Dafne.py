# Ejercicio 1
print("------ Ejercicio 1 -----")
def f(n):
    if n <= 0:
        return "Inserta un entero mayor que cero"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    v1, v2 = 0, 1
    for x in range(n-2):
        v1, v2 = v2, v1 + v2
    return v2

n = int(input("inserta un número: "))
valor_f = f(n)
print("Valor del enésimo término de Fibonacci: ", valor_f)

# Ejercicio 2
print("------ Ejercicio 2 -----")
def f2(n):
    if n <= 0:
        return "Inserta un entero mayor que cero"

    v1, v2 = 0, 1
    sf = []
    for x in range(n):
        sf.append(v1)
        v1, v2 = v2, v1 + v2
    return sf

n = int(input("inserta un número: "))
valor_f = f2(n)
print("Los", n, "términos de la serie de Fibonacci son:", valor_f)

# Ejercicio 3

print("-----Ejercicio 3 -----")

a = int(input("Valor inicial de Watson:"))
b = int(input("Valor final de Watson:"))

if a > b:
    print("Rango inválido")
else:
    contador = 0
    n = 1

    while n * n <= b:
        if n * n >= a:
            contador += 1
        n += 1

print("La respuesta de Sherlock es:", contador)

# Ejercicio 4
print("------ Ejercicio 4 ------")

s = input("Ingresa una cadena de letras en minúscula: ")
n = int(input("Ingresa un entero: "))

contar_a = s.count('a')

len_s = len(s)

reps_total = n // len_s

letras_restantes = n % len_s

# Contar 'a' en las repeticiones completas
total_a = reps_total * contar_a

# Contar 'a' en las letras restantes
total_a += s[:letras_restantes].count('a')

print(total_a)

