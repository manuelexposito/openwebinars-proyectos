#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cadena=input("Di una frase: ")
subcadena=input("Di qué carácter quieres buscar en la frase: ")

while True:

    if len(subcadena) == 1:
        print("Número de veces que aparece %s : %d" % (subcadena, cadena.count(subcadena)))
        break
    else:
        print("Solo puede ser un carácter.")
        subcadena=input("Di cual quieres buscar en la frase: ")