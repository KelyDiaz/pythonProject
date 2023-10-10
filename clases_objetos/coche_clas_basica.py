class Coche:
    marca = ""
    color = "Blanco"

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color


# Aca se esta instanciando la clase
coche1 = Coche("Toyota", "Negro")
#Se modifica una variable del objeto
coche1.color="Azul"
coche_lujo = Coche("BMW", "Plata")

print(f'Marca: {coche1.marca}, Color: {coche1.color}')
print(f'Marca: {coche_lujo.marca}, Color: {coche_lujo.color}')
