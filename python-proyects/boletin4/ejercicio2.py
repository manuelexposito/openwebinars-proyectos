#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

texto = input("Di una palabra: ")

subcadena=input("¿Por qué letra empieza? :")


while True :
    if texto.startswith(subcadena):
        print("Eso es correcto.")
        break
    else: 
        print("No, eso es incorrecto.")
        texto = input("Di una palabra: ")
        subcadena=input("¿Por qué letra empieza? :")

print("Programa finalizado")