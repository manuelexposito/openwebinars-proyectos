#Algoritmo que pida tres números y los
#muestre ordenados (de mayor a menor);

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))

mayorNum = num1
midNum = int
menorNum = int

if num2 > mayorNum:
    mayorNum = num2
    menorNum = num1
elif num2 < mayorNum:
    mayorNum = num1
    menorNum = num2


if num3 > mayorNum:
    midNum = mayorNum
    mayorNum = num3
elif num3 < menorNum:
    midNum = menorNum
    menorNum = num3
elif num3 < mayorNum and num3 > menorNum:
    midNum = num3

    


print("El orden de los números es: ")
print(mayorNum)
print(midNum)
print(menorNum)

