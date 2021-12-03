#Escribe un programa que pida un nombre de usuario
# y una contraseña y si se ha introducido “pepe” y “asdasd” 
#se indica “Has entrado al sistema”, sino se da un error.

nombre = "pepe"
password = "asdasd"

nombreInp=input("Introduzca el nombre: ")
passwordInp=input("Introduzca la contraseña: ")

if nombre == nombreInp and password == passwordInp:
    print("Has entrado en el sistema")
elif nombre != nombreInp:
    print("Error: El nombre no es correcto")
elif password != passwordInp:
    print("Error: La contraseña no es correcta")