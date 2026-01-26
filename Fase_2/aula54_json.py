import json

caminho = 'C:\\Users\\João Victor\\Desktop\\fundamentos-python\\Fase_2\\'
nome = caminho + 'aula54.json'

# pessoa = {
#     'nome': 'João Victor',
#     'idade': 19,
#     'endereco': [
#         {'rua': 'rua da amargura', 'numero': '100'},
#         {'rua': 'rua da lamasal', 'numero': '190'}
#     ],
#     'altura': 1.7,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'nada': None
# }

# with open(nome, 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, indent= 4)


# ocorre mudança de estruturas: tupla -> array por exemplo
with open(nome, 'r') as arquivo:
    pessoa_carregada = json.load(arquivo)
    print(pessoa_carregada)

