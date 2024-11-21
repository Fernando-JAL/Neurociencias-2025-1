# EJERCICIO 1:
'''En un solo lanzamiento de dos dados de 6 caras (con el mismo peso), encuentre la probabilidad de que su
suma sea como máximo n. Cree una funcion llamada 'lanzamiento' que reciba un entero llamado 'n' y retorne un
flotante que calcule la probabilidad de que el lanzamiento de 2 dados de 6 caras sea <= n.'''

n = int(input('INTRODUSCA EL VALOR DE n: '))
con_tot = 36
casos= 0

def lanzamiento(n):
    global casos
    for d1 in range(1,7):
        for d2 in range(1,7):
            sum = d1 + d2
            if sum <= n:
                casos += 1
            else:
                continue
    return casos

lanzamiento(n)
prob= casos/con_tot

print(f'EL NUMERO DE CASOS DONDE LA SUMA<={n} ES DE {casos}, Y LA PROBABILIDAD ES DE {prob}')
