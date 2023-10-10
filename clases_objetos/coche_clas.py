class Coche:
    marca = ""
    color = "blanco"

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color


# Aca se esta instanciando la clase
coche1 = Coche("toyota", "negro")
coche_lujo = Coche("BMW", "Plata")

print(f'Marca: {coche1.marca}, Color: {coche1.color}')
print(f'Marca: {coche_lujo.marca}, Color: {coche_lujo.color}')
