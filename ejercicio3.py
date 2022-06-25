"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

"""

class Triangulo:

    def __init__(self):
        self.lado1=float(input("Ingrese el lado 1 del triangulo: "))
        self.lado2=float(input("Ingrese el lado 2 del triangulo: "))
        self.lado3=float(input("Ingrese el lado 3 del triangulo: "))
        print("-------------------------------")
    
    def tipoTriangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("El triangulo es: Equilatero")
        elif self.lado1 != self.lado2 and  self.lado1 != self.lado3:
            print("El triangulo es: Escaleno")
        else:
            print("El triangulo es: Iscoceles")
    
    def esMayor(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Sus 3 lados son iguales")
        elif self.lado1 > self.lado2 and  self.lado1 > self.lado3:
            print("El lado mayor mide: ", self.lado1)
        elif self.lado2 > self.lado1 and  self.lado2 > self.lado3:
            print("El lado mayor mide: ", self.lado2)
        else:
           print("El lado mayor mide: ", self.lado3)
    

#Bloque principal

triangulo1 = Triangulo()
triangulo1.esMayor()
triangulo1.tipoTriangulo()