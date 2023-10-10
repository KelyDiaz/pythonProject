class Coche:
    marca = ""
    color = "Blanco"
    encendido = False
    velocidad =0

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender(self):
        self.encendido = True

    def set_velocidad(self, velocidad):
        self.velocidad= velocidad


# Aca se esta instanciando la clase
coche1 = Coche("Toyota", "Negro")
# Se modifica una variable del objeto
coche1.color = "Azul"
coche1.encender()
coche1.set_velocidad(40)
coche_lujo = Coche("BMW", "Plata")

print(f'Marca: {coche1.marca}, Color: {coche1.color}')
print(f'Marca: {coche_lujo.marca}, Color: {coche_lujo.color}')

if coche1.encendido:
    print(f"prendido y va a una velocidad de {coche1.velocidad} km/h")
    coche1.set_velocidad(100)
    print(f"prendido y va a una velocidad de {coche1.velocidad} km/h")
else:
    coche1.encender()
    print("apagado")
