#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
#Escribir un algoritmo que determine la hora de llegada a la ciudad B.

#Se le pasa hora con minutos y segundos. Se convierten a SEGUNDOS. 

horaSalida= int(input("Diga la hora a la que sale: "))
minutosSalida= int(input("Diga el minuto en el que sale: "))
segundosSalida= int(input("Diga los segundos en los que sale: "))

segundosTotalesSalida = ((horaSalida*60)*60) + (minutosSalida*60) + segundosSalida

#Pedimos cuanto tarda en llegar

tiempoEnLlegar= int(input("Diga cuantos segundos tarda en llegar: "))

#Devolvemos el resultado en HORAS, MINUTOS y SEGUNDOS

horaLlegada = ((segundosTotalesSalida + tiempoEnLlegar) // (60 * 60))

minutosLlegada = ((segundosTotalesSalida + tiempoEnLlegar) % (60 * 60)) // 60

segundosLlegada = ((segundosTotalesSalida + tiempoEnLlegar) % (60 * 60)) % 60

print("El ciclista llega a las %d : %d : %d" % (horaLlegada, minutosLlegada, segundosLlegada))