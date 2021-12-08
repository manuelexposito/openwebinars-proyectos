#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

cadena = input("Diga la cadena: ")

dic = {}
nuevoDic = {}
cadena = cadena.lower().strip()

#contar las veces que aparece cada caracter

cadenaOrdenada = sorted(cadena)
letraAnterior = ""
contadorLetra = 0

for c in cadenaOrdenada:

    if c == letraAnterior:
        contadorLetra+=1
        
    else:
        contadorLetra = 1
        letraAnterior = c

    nuevoDic = { c : contadorLetra}
    dic.update(nuevoDic)

#Mostrarlos en forma de lista
for clave,valor in dic.items():
    print(clave, valor)