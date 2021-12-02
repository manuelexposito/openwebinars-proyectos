#Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
#Dicha calificación se compone de los siguientes porcentajes:

# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

#55%
parcial1=float(input("Nota de su parcial1 :"))
parcial2=float(input("Nota de su parcial2 :"))
parcial3=float(input("Nota de su parcial3 :"))

porcentajeParciales= (parcial1 + parcial2 + parcial3) / 3 * (55 / 100)
#30%
examenFinal=float(input("Nota del examen final: "))

porcentajeExamen = examenFinal * (30/100)
#15%
trabajoFinal=float(input("Nota del trabajo final: "))

porcentajeTrabajo = trabajoFinal * (15/100)

print("Su nota final es de %.2f" % (porcentajeParciales + porcentajeExamen + porcentajeTrabajo))