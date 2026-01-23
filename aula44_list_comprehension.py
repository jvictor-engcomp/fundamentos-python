lista = [numero*2 for numero in range(10)]
#print(lista)

#mapeamento de dados com list comprehension, if na esquerda do for

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'nome': produto['nome']+'_novo', 'preco': produto['preco'] * 1.1}
    if produto['preco'] < 30 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep = '\n')

#filtro, if depoisdo for 

novos_produtos = [
    {**produto, 'nome': produto['nome']+'_novo', 'preco': produto['preco'] * 1.1}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

print(*novos_produtos, sep = '\n')

#list comprehension com mais de um for

lista = [
    (x, y, z)
    for x in range(3)
    for y in range(3)
    for z in range(3)
    if x != 2 and y != 2 and z !=2 
] # gera valores binários de 0 a 7

print('\n', lista)
