# Examen 3er parcial. dataframes y grafos

### Instrucciones para subir examen

En repo Neurociencias-2025-1:

- Estar en branch main
- Actualizar repo
- Crear branch con nombre parcial_3ro_nombre
- Cambiarse a su branch, checkout
- Dentro del folder de Parcial_3ro agregar los archivos:
	- ej1_nombre
	- ej2_nombre
	- ej3_nombre
	- ej4_nombre
	- ej5_nombre
- Hacer commit de solo los archivos del examen
- Hacer pull del commit que solo tiene los archivos del examen
- Hacer pull request con el nombre Examen_3er_parcial_nombre


## Ejercicio 1.
En un solo lanzamiento de dos dados de 6 caras (con el mismo peso), encuentre la probabilidad de que
su suma sea como máximo $n$.
Cree una funcion llamada 'lanzamiento' que reciba un entero llamado 'n' y retorne un flotante que calcule la
probabilidad de que la suma de las caras al lanzar 2 dados de 6 caras sea <= n.

### Escriba su código aquí

## Ejercicio 2. 
Analice el código en los archivos animation2_1 y animation2_2 y conteste lo siguiente:
- ¿Qué forma tiene el grafo?
- ¿Cuántos nodos tiene el grafo?, ¿con qué comando descubres el número de nodos?
- ¿Cuántas aristas tiene el grafo?, ¿con qué comando descubres el número de nodos?
- ¿Qué hace el código G.degree()?
- ¿Cuál es el número máximo de aristas en el grafo?
- ¿Cuál es la diferencia entre animation2_1 y animation2_2?

## Ejercicio 3.
Modifique el código de animation2_2 para usar la información de 'fve30.mat'.
Para las coordenadas 'x', 'y', 'z' utiliza un arreglo de números enteros aleatorios en el intevalor [0, 50]

## Ejercicio 4.
Para los datos de 'Coactivation_matrix.mat', filtre la matriz para obtener los valores > 0.2, con el nuevo 
arreglo muestre los nodos y vértices del grafo ploteado en 3D

## Ejercicio 5.
Para los datos de 'Coactivation_matrix.mat', filtre la matriz para que, para cada nodo, se mantenga aquel nodo 
con mayor comunicación, con el nuevo arreglo muestre los nodos y vértices del grafo ploteado en 3D

