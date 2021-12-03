#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre=input("Diga su nombre: ")
apellido1=input("Diga su primer apellido: ")
apellido2=input("Diga su segundo apellido: ")

inicialNombre = nombre[0].upper()
inicialApellido1 = apellido1[0].upper()
inicialApellido2 = apellido2[0].upper()

print("Sus iniciales son: %s.%s.%s."%(inicialNombre, inicialApellido1, inicialApellido2))