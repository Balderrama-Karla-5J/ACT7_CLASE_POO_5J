print("Programacion POO")
# Definicion de clases
class Perro:
    #Funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self, nombre, edad):
        print(f"Nombre: {nombre} Edad: {edad}" )

#Zona de creacion de objeto

labrador = Perro()

#Zona de uso de objetos

labrador.Datos_perro("Pecas", 3)
labrador.morder()