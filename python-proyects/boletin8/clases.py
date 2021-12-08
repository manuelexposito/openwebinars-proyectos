class Persona():
 
    def _init_(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        
        if edad > 0 and edad < 100:
            self._edad = edad
        else:
            print("No puedes registrar a alguien con esa edad.")
    
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        
       self._dni = dni    
    
    
    def mostrar(self):
        
        return self.nombre + " | " + str(self.edad) + " | " + self.dni.mostrar()
    
    
    def esMayorDeEdad(self):
        
        if self._edad >= 18:
            return True
        else:
            return False


class Dni():
    
    def _init_(self, numeros, letra):
        self.numeros = numeros
        self.letra = letra
    
    def _calcular_letra(self):
        letras ='TRWAGMYFPDXBNJZSQVHLCKE'
        return letras[int(self.numeros)%23]
    
    @property
    def numeros(self):
        return self._numeros
    
    @numeros.setter
    def numeros(self, numeros):
        if len(numeros) == 8:
            self._numeros = numeros
            self._letra = self._calcular_letra()
        else:
            self._numero = 0
            self._letra = ""
            print("DNI incorrecto.")
            
    
    @property
    def letra(self):
        return self._letra
    
    @letra.setter
    def letra(self, letra):
       
       self._letra = letra
       
    def mostrar(self):
        
        return self.numeros + self.letra
       
       
       
       
class Cuenta():
    
    def _init_(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        
    @property
    def titular(self):
        return self._titular.mostrar()
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
        
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad
        
    def mostrar(self):
        
        return self.titular.mostrar()+ " | " + str(self.cantidad)
    
   
    def ingresar(self, dinero):
        
        self.cantidad += dinero
    
    
    def retirar(self, dinero):
        
        self.cantidad -= dinero
        
        
        
class CuentaJoven(Cuenta):
    
    def _init_(self, titular, cantidad, esValido):
        super(titular,cantidad)
        self.esValido = esValido
        
    def _esValido(self):
        if self.titular.esMayorDeEdad:
            self._esValido = True
        else:
            self._esValido = False
            
    def retirar(self, cantidad):
        
        if self.esValido:
            super().retirar(self, cantidad)
            
        else:
            print("Debes ser mayor de edad para realizar esta acción.") 

    def mostrar():
        
        return super().mostrar 