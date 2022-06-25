class Cuenta:
    titular = ""
    cantidad = ""

    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad=float(cantidad)
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def Settitular(self,titular):
        self.__titular =titular
    
    # @cantidad.setter
    # def Setcantidad(self,cantidad):
    #     self.__cantidad =cantidad

    def mostrar(self):
        print("Nombre del titular: " + str(self.titular))
        print("Cantidad: " + str(self.cantidad))
        if CuentaJoven.esTitularValido(self) == True:
            print("Es cuenta joven")
        else:
            print("Cuenta corriente")
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
            print("cantidad ingresada correctamente")
        else:
            print("Imposible introducir esa cantidad")
    
    def retirar(self,cantidad):
        if CuentaJoven.esTitularValido(self) == True:
            self.__cantidad = self.__cantidad - cantidad
        else:
            print("No es posible retirar el dinero")




class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion,edad):
        super().__init__(titular, cantidad)
        self.__bonificacion = float(bonificacion)
        self.__edad = edad
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @property
    def edad(self):
        return self.__edad
    
    @bonificacion.setter
    def Setbonificacion(self,bonificacion):
        self.__bonificacion =bonificacion

    @edad.setter
    def Setedad(self,edad):
        self.__edad =edad

    def esTitularValido(self):
        if self.edad >= 18 and self.edad <= 25:
            return True
        else:
            return False
    
    def imprimir(self):
        print("-------------------")
        super().mostrar()
        print("Bonificacion de cuenta: ", self.bonificacion)



# cliente1 = Cuenta("fer", 600)
# cliente1.mostrar()
# cliente1.ingresar(300)
# cliente1.retirar(100)
# cliente1.mostrar()

cliente2=CuentaJoven("fer", 600,0.2,20)
cliente2.mostrar()
print(cliente2.esTitularValido())
cliente2.retirar(100)
cliente2.imprimir()