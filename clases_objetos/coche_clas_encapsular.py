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

"""Aca se esta instanciando la clase"""
coche1 = Coche("Toyota", "Negro")

""" Se modifica una variable del objeto """
coche1.encender()
# coche1.__encendido

print(f'Marca: {coche1.marca}, Color: {coche1.color}')
print(f'Encendido: {coche1.get_encendido()}')

