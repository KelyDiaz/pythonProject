tabla = int(input('¿Qué tabña quieres ver: '))
nums = range(0, 11)

for num in nums:
    valor = num * tabla
    print(f'{tabla} x {num} = {valor}')
