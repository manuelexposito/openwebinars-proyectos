#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

num=int(input("Diga un número: "))
suma = 0
contador = 0
media = 0

while num != 0:
    suma = num + suma
    contador +=1
    num=int(input("Diga un número: "))


if contador != 0:
    media = suma / contador

print("La suma ha sido %d, y la media ha sido: %.2f"%(suma, media))