"""
Realizar un programa que tenga una clase Persona con las siguientes características. La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.
"""

class Persona:
    
    def __init__(self):
        self.nombre=input("Ingrese su nombre: ")
        self.edad=int(input("Ingrese su edad: "))
        print("-------------------------------")
    def mostrar (self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("-------------------------------")
    def esMayor(self):
        if self.edad >=18:
            print(self.nombre, " Es mayor de edad")
        else:
            print(self.nombre, " Es menor de edad")


#Bloque principal
persona1 = Persona()
persona1.mostrar()
persona1.esMayor()