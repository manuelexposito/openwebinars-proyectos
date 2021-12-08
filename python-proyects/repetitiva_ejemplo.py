secreto = "elsecreto"
clave = input("Dime la clave: ")
intentos = 0
while clave != secreto and intentos < 2:
    
    print("Clave incorrecta")
    clave = input("Dime la clave: ")
    intentos = intentos+1

    if intentos >= 2:
        print("Se agotaron sus intentos. Pruebe más tarde.")


if clave == secreto:
        print("Correcto, puede pasar.")
print("Programa terminado")