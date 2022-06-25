"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

"""

class Alumno:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del alumno: ")
        self.nota=int(input("Ingrese la calificación del alumno: "))
        print("-------------------------------")
    def mostrar (self):
        print("Nombre del alumno: ", self.nombre)
        print("Calificacion del alumno: ", self.nota)
        print("-------------------------------")
    def calificacion(self):
        if self.nota >= 8:
            print("La calificacion: ", self.nota , " es aprobatoria")
        else:
            print("El alumno con calificacion: ", self.nota , " esta reprobado")
    

#bloque principal

alumno1 = Alumno()
alumno1.mostrar()
alumno1.calificacion()
