#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
#(comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media,
#la nota más alta que ha sacado y la menor.

lista = []
nota = int

while len(lista) < 5:
    
    nota = int(input("Diga la nota del alumno: "))
    if nota <= 10 and nota >= 0:

        lista.append(nota)
    else: 
        nota = int(input("Número no válido. \nDiga la nota del alumno: "))


print("Notas: ", lista)
print("Nota media: %.2f | Mayor nota: %d | Menor nota: %d" % ((sum(lista)/5), max(lista), min(lista)))