
class Persona(object):
    nombre = ""
    edad = ""
    curp = ""

    def __init__(self, nombre, edad, curp): 
        self.__nombre = nombre 
        self.__edad = edad
        self.__curp = curp


    @property
    def nombre(self): 
        return self.__nombre 

    @property
    def edad(self):
        return self.__edad
    
    @property
    def curp(self):
        return self.__curp

    @nombre.setter 
    def Setnombre(self,nombre):
        self.__nombre = nombre
    
    @edad.setter
    def Setedad (self,edad):
        self.__edad = edad
    
    @curp.setter
    def Setcurp (self,curp):
        self.__curp = curp

    def mostrar(self):
        print("Nombre: " + str(self.nombre))
        print("Edad: " + str(self.edad))
        print("Curp: " + str(self.curp))

    def esMayor(self):
        if self.edad >= 18:
            return True
        else:
            return False

#Bloque principal
persona1 = Persona('fer', 22 , 'HEVF5465OP3')
persona1.mostrar() 
print(persona1.esMayor())
