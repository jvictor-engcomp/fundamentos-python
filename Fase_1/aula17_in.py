nome = 'joao victor araujo soares'
encontrar = input('O que quer encontrar no nome? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
