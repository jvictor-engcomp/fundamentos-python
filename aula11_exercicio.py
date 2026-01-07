nome = 'joao victor'
altura = 1.69
peso = 60
imc = peso / (altura ** 2)

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f"pesa {peso}kg"
linha_3 = f"e seu imc vale {imc:.2f}"
print(linha_1)
print(linha_2)
print(linha_3)