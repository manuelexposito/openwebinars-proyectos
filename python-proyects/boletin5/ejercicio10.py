#Diseñar el algoritmo correspondiente a un programa, que:

#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

from random import randint

tabla = []
num = int
num2 = int
for i in range(0,5):
    num = randint(1, 9)
    
    for j in range(0,5):
        num2 = randint(1,9)
        tabla.append([num , num2])
        print(num, "", num2, end="")

#print(tabla)