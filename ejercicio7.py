"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés.
Crear al menos un objeto de cada subclase.

"""

class Cuenta:
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Titular: ", self.titular)
        print("Cantidad: ", self.cantidad)



class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes=interes

    def ganancias(self):
        total = self.cantidad*self.interes/100
        print("El importe de interes es: ", total)
    
    def imprimir(self):
        print("-----------------")
        print("Cuentas a plazo fijo")
        super().mostrar()
        print("Dias de plazo: ", self.plazo)
        print("Interes: ", self.interes)
        self.ganancias()

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)
    
    def imprimir(self):
        print("-----------------")
        print("Cuenta de caja de ahorros")
        super().mostrar()


cajita = CajaAhorro("Fer", 600)
cajita.imprimir()

plazo = PlazoFijo("Fernando", 10000, 365 , 1.3)
plazo.imprimir()