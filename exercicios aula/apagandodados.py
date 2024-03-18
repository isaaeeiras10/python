carros = ['Vectra', 'Astra', 'Palio', 'Saveiro', 'Masserati']

#contar itens primeiro 
count = len(carros)

#Loop for exibir itens com range(count)
for idx in range(count):
    print(idx, carros[idx])

apagar = int(input("apague um: "))
del carros[apagar]

for idx in range(count):
    print(idx, carros[idx])