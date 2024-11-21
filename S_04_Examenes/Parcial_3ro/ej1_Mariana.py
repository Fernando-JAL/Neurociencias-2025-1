#En un solo lanzamiento de dos dados de 6 caras (con el mismo peso),
# encuentre la probabilidad de que su suma sea como máximo n
#Cree una funcion llamada 'lanzamiento' que reciba un entero llamado 'n' y retorne un flotante que calcule la probabilidad de que el lanzamiento de 2 dados de 6 caras sea <= n.

def lanzamiento(n):
    casos = 0
    for dado1 in range(1, 7):
        for dado2 in range(1, 7):
            if dado1 + dado2 <= n:
                casos += 1
    return casos

# Solicitar el valor de n al usuario
n = int(input('Introduzca el valor del 1 al 6: '))
con_tot = 36
casos = lanzamiento(n)
prob = casos / con_tot

print(f'El númuero de casos done la suma <= {n} es de  {casos}, y su probabilidad de  {prob:.4f}')