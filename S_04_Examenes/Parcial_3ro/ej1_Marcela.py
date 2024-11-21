# Ejercicio 1
def lanzamiento (n):
    if n >= 12:
        print(36)
    else:
        count=0
        for dado1 in range(1,7):
            for dado2 in range(1,7):
                suma = dado1+dado2
                if suma <= n:
                    count+=1
                else:
                    continue
        print(count)

lanzamiento(11)

