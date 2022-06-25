"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

"""

class Calculadora:
    def __init__(self):
        self.valor1=float(input("Digita el valor 1: "))
        self.valor2=float(input("Digita el valor 2: "))

    def suma(self):
        suma = self.valor1 + self.valor2
        print("La suma es: ", suma)
    
    def resta(self):
        resta = self.valor1 - self.valor2
        print("La resta es: ", resta)
    def multiplicar(self):
        multi = self.valor1 * self.valor2
        print("La multiplicacion es: ", multi)
    def dividir(self):
        divide = self.valor1 / self.valor2
        print("La division es: ", divide)


#Bloque principal
calculo1 = Calculadora()
calculo1.suma()
calculo1.resta()
calculo1.multiplicar()
calculo1.dividir()
    
