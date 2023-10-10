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