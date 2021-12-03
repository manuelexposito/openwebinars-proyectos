# Calcular el perímetro y área de un rectángulo dada su base y su altura.

#Base * Altura / 2

base = float(input("Base del rectángulo: "))
altura= float(input("Altura del rectángulo: "))

print("El perímetro es %.2f y el área es %.2f" % ((2*base + 2*altura), (base*altura/2)))