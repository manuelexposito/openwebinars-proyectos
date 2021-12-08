#El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido 
#desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha 
#nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

#LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#EsBisiesto: Recibe un año y nos dice si es bisiesto.
#Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.


def leerFecha():

    dia= int(input("Di el día: "))
    mes= int(input("Di el mes: "))
    anio= int(input("Di el año: "))
    
    return dia, mes, anio


def diasDelMes(mes, anio):

    dias = 0
    
    #if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias = 31
        #print("Ese mes tiene 31 días")
    #elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    elif mes in [4, 6, 9, 11]:   
        dias = 30
        # print("Ese mes tiene 30 días")
    elif mes == 2:
        
        if esBisiesto(anio):
            dias = 28
            #print("Al ser este año bisiesto, febrero tiene 29 días")
        else:
            dias = 28
            #print("Ese mes tiene 28 días")
            
    else:
        print("Ese mes no existe")
        
    return dias


def esBisiesto(anio):

    if anio % 4 != 0: #no divisible entre 4
        return False
    elif anio % 4 == 0 and anio % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: #divisible entre 4 y 10 y no entre 400
        return False
    elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: #divisible entre 4, 100 y 400
        return True


def calcularDiaJuliano(dia, mes, anio):
       
    diaJuliano = 0
    
    for m in range(1, mes):
        
        diaJuliano += diasDelMes(mes, anio)
        
    diaJuliano += dia
    return diaJuliano

    

dia, mes, anio = leerFecha()
esBisiesto(anio)
diasDelMes(mes, anio)

print("Días Julianos: ", calcularDiaJuliano(dia, mes, anio) )
