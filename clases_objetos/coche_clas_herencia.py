class Coche:
    marca = ""
    color = "Blanco"
    __encendido = False

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.__encendido = True

    def get_encendido(self):
        return self.__encendido


# herencia de una clase a otra
class CocheDeportivo(Coche):
    cv = 60

    def __init__(self, marca, color, cv):
        self.marca = marca
        self.color = color
        self.cv = cv


"""Aca se esta instanciando la clase"""
coche1 = Coche("Toyota", "Negro")

""" Se modifica una variable del objeto """
coche1.encender()
# coche1.__encendido

coche_lujo = CocheDeportivo("BMW", "Negro", 200)
print(f'Marca: {coche_lujo.marca}, Color: {coche_lujo.color}, CV: {coche_lujo.cv}')

print(f'Marca: {coche1.marca}, Color: {coche1.color}')
print(f'Encendido: {coche1.get_encendido()}')
