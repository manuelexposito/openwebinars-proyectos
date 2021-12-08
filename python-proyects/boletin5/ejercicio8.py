#Queremos guardar los nombres y la edades de los alumnos de un curso. 
#Realiza un programa que introduzca el nombre y la edad de cada alumno. 
#El proceso de lectura de datos terminará cuando se introduzca como
#nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

#Todos lo alumnos mayores de edad.
#Los alumnos mayores (los que tienen más edad)


nombre = str 
edad = int
cont = 0
listaAlumnos = []
edades = []

while True:


    nombre = input("Diga el nombre del alumno %d: " % (len(listaAlumnos) + 1))
    if nombre != "*":
        edad = int(input("Diga la edad del alumno %d: " % (len(listaAlumnos) + 1)))

        listaAlumnos.append([nombre, edad])
    else:
        break
    
    
print(listaAlumnos)

print("--------------------------")
print("Alumnos MAYORES DE EDAD")
for i in listaAlumnos:
    if i[1] >= 18:
        print(i[0])

print("--------------------------")
print("Alumnos MAYORES")
for i in listaAlumnos:
    edades.append(i[1])

for i in listaAlumnos:
    if i[1] == max(edades):
        print(i[0])

    
    
