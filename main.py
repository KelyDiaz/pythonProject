lista = ["hola", "kely"]
t_prueba = ("prueba", 3)
lista.insert(1, "diaz")
data = {'nombre': 'kely', 'edad': 27}
data['ciudad'] = "ocaña"
print(f"mi nombre es {data['nombre']} y edad es {data['edad']}")
print(data)
del data['edad']
print(len(data))
print(data)
edad = int(input("Ingresa la edad: "))
array20items = range(0,20)
if not edad == 16:
    print("bienvenido")

for elem in array20items:
    print(elem)
