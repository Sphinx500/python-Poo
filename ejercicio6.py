"""
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.

"""


class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0
    
    def depositar(self,monto):
        self.monto = self.monto + monto
    
    def extraer(self, monto):
        self.monto = self.monto - monto
    
    def montos(self):
        return self.monto
    
    def imprimir_saldo(self):
        print(self.nombre, " Tiene una cantidad de: ", self.monto)


class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Fernando")
        self.cliente2 = Cliente("Liz")
        self.cliente3 = Cliente("Alex")

    def operar(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(2500)
        self.cliente3.depositar(100)
        self.cliente1.extraer(500)
        self.cliente2.depositar(200)
    
    def deposito_total(self):
        total = self.cliente1.montos() + self.cliente2.montos() + self.cliente3.montos()
        print("El total en el banco es de:", total)
    

banco = Banco()
banco.operar()
banco.deposito_total()
