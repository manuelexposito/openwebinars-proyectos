#Algoritmo que pida dos números e 
#indique si el primero es mayor que el segundo o no.

num1=int(input("Diga el primer numero: "))
num2=int(input("Diga el segundo numero: "))

if num1 > num2:
    print("El mayor es el primer número")
elif num2 > num1:
    print("El mayor es el segundo número")
else:
    print("Son el mismo número")