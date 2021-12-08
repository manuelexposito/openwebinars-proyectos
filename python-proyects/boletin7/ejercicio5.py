#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
#Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista): 
    return max(lista), min(lista)

num = int
lista = []

while len(lista) < 10:

    while True:
        try:
            num = int(input("Di un número: "))
            
            lista.append(num)
            break
           
        except ValueError:
            print("Debes introducir un número")


print("El mayor es", calcularMaxMin(lista)[0])
print("El menor es", calcularMaxMin(lista)[1])
