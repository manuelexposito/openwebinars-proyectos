#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

num = int(input("Diga un número: "))

for var in range(1, 11):

    print("%d X %d = %d" % (num, var, (var*num)))