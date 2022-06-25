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
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
            print("cantidad ingresada correctamente")
        else:
            print("Imposible introducir esa cantidad")
    
    def retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad

cliente1 = Cuenta("fer", 600)

cliente1.mostrar()
cliente1.ingresar(300)
cliente1.retirar(100)
cliente1.mostrar()


