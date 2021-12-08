#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
#Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def esMultiplo(a, b):
    
    if a % b == 0:
        return True
    else:
        return False

num = int(input("Di un número: "))
num2 = int(input("Di el otro número: "))

if esMultiplo(num, num2):
    print("El segundo número es múltiplo del primero.")
else:
    print("El segundo NO es múltiplo del primero.")
