#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

from random import randint


lista = []


for i in range(0, 10):

    lista.append(randint(1,10))
    print("Número: %d | Cuadrado: %.2f | Cubo: %.2f" % (lista[i], lista[i] ** 2, lista[i] ** 3))

