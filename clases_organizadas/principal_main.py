"""Importa todas las clases y demas que tenga el fichero"""
# import coche
"""Importa solo la clase que necesito del fichero"""
# from coche import Coche
"""Importa solo la clase que necesito del fichero que esta en otra carpeta"""
# from Clases.coche import Coche

"""Importa varias clses que necesito del fichero coche"""
from coche import Coche, CocheDeportivo

coche1 = Coche("Toyota", "Negro")

print(f'Marca: {coche1.marca}, Color: {coche1.color}')

coche_lujo = CocheDeportivo("BMW", "Negro", 200)
print(f'Marca: {coche_lujo.marca}, Color: {coche_lujo.color}, CV: {coche_lujo.cv}')

