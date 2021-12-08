#Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de 
#las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos 
#mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta 
#no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

lista_frutas = {"manzana" : 0.80, "pera" : 0.75, "piña" : 1.50, "mandarinas" : 0.45, "naranjas" : 0.70}

opcion = str

while True:

    fruta = input("¿Qué fruta busca? :")

    while fruta.lower() not in lista_frutas:
        print("La fruta que usted dice no se encuentra en la base de datos. Estas son las frutas registradas: ")
        for fruta in lista_frutas.keys():
            print(fruta)
        fruta = input("Diga cual de estas busca: ") 

    if fruta in lista_frutas:

        while True:
            try:
                cantidad = int(input("¿Cuántas piezas de %s se han vendido?: " % fruta))
                print("El precio final es de : %.2f €" % (lista_frutas[fruta] * cantidad))
                break
            except ValueError:
                print("Debes introducir un número")

    opcion= input("¿Desea hacer otra consulta? S/N: ")

    if opcion.lower() == "n":
        print("¡Hasta otra!")
        break




   


