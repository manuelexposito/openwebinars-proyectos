# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:

        #C = (F-32)*5/9

f = float(input("Diga los grados en Fahrenheit: "))

print("%.2f Fº son %.2f Cº" % (f, ((f-32)*5/9)))