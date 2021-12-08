#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena = input("Diga una cadena: ")
subc = input("Diga una subcadena: ")

if subc in cadena:

    print("La subcadena se encuentra dentro de la cadena.")
else: 
    print("No, la subcadena no está dentro de esa cadena.")