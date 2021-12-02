#Dadas dos variables numéricas A y B, que el usuario debe teclear, 
#se pide realizar un algoritmo que intercambie los valores de ambas
#variables y muestre cuanto valen al final las dos variables.

a=int(input("Diga la variable A: "))
b=int(input("Diga la variable B: "))

c = int(a) 

a = b

b = c 

print("La variable A ahora es %d y la variable B ahora es %d" %(a, b))