"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda

"""

class Agenda:
    def __init__(self):
        self.contactos={}
    
    def nuevoContacto(self):
        nombre = input("Inserte el nombre del contacto: ")
        telefono = int(input("Inserte el numero de telefono: "))
        correo = input("Inserte el email del contacto: ")
        contacto = {"telefono":telefono,"correo":correo}
        self.contactos[nombre] = contacto
        print("El contacto se ha guardado")

    def buscarContacto(self):
        busqueda = input("Ingrese el nombre de contacto: ")
        for i in self.contactos[busqueda]:
            print(self.contactos[busqueda][i])
    
    def listaContactos(self):
        for i in self.contactos:
            print(i)
            for k in self.contactos[i]:
                print("numero: ", self.contactos[i].get("telefono"))
                print("correo electronico: ", self.contactos[i].get("correo"))
    
    def eliminaContacto(self):
        elim=input("Ingrese el contacto a elminar: ")
        self.contactos.pop(elim)


miAgenda = Agenda()

while True:
    try:
        op=int(input("Elija la operacion a realizar: "))
        print("-------------------")
        print("1.Añadir contacto")
        print("2.Lista de contactos")
        print("3.Buscar contacto")
        print("4.Editar contacto")
        print("5.Cerrar agenda")
        print("-------------------")

        if op == 1:
            miAgenda.nuevoContacto()
        elif op == 2:
            miAgenda.listaContactos()
        elif op == 3:
            miAgenda.buscarContacto()
        elif op == 4:
            miAgenda.eliminaContacto()
        elif op == 5:
            break
        else:
            print("Por favor elige una opcion")
            op=int(input("Elija la operacion a realizar: "))

    except ValueError:
        print("Solo se aceptan numeros del 1 al 5")


