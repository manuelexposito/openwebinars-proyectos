#Escribir un algoritmo para calcular la nota final de un estudiante, 
#considerando que: por cada respuesta correcta 5 puntos, por una incorrecta 
#-1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

rCorrectas=int(input("Di cuantas son correctas: "))
rIncorrectas=int(input("Di cuantas son incorrectas: "))
rBlancas=int(input("Di cuantas están en blanca: "))

print("Su puntuación es de %d" % ((rCorrectas * 5)+(rIncorrectas * -1)))