#Suponiendo que hemos introducido una cadena por teclado que representa una frase 
#(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

frase = input("Diga una frase: ")

print("Su frase tiene %d palabras" % len(frase.split()))

