nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

numero_espacos = 0

if nome and idade:

    for i in range(len(nome)):
        if nome[i] == ' ':
            numero_espacos = numero_espacos + 1
    
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome) - numero_espacos} letras')
    print(f'A última letra do seu nome é {nome[len(nome) - 1]}')
    print(f'A primeira letra do seu nome é {nome[0]}')
else:
    print('Desculpe, você deixou algum campo vazio')    


