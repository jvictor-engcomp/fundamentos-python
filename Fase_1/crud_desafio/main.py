import dados, services
import os
from time import sleep

services.cabecalho()
sleep(2)

while True:
    print()
    services.opcoes()
    choice = input("Escolha: ")

    if choice == '1':
        os.system('cls')

        print('Digite as informações')
        id = input('Id: ')
        nome = input('Nome: ')
        email = input('Email: ')

        if not id.isdigit() or not nome.isalpha():
            print('Entradas inválidas')
            continue
        if services.criar_usuario(id, nome, email) is None:
            print('Id ou Email já foi usado')
            continue

        
        print('Usuário criado com sucesso!')

    elif choice == '2':
        os.system('cls')
        if services.listar_usuarios_ativos(dados.lista_todos_usuarios)\
        == -1:
            print('Lista vazia')

    elif choice == '3':
        os.system('cls')

        id = input('Digite a Id: ')
        if services.buscar_id(id, dados.lista_todos_usuarios) == -1:
            print('Lista vazia')
        if services.buscar_id(id, dados.lista_todos_usuarios) == None:
            print('Usuário não encontrado')
        else: 
            print(*services.buscar_id(id, dados.lista_todos_usuarios).values())

    elif choice == '4':
        os.system('cls')
        
        id = input('Digite a Id: ')
        if services.buscar_id(id, dados.lista_todos_usuarios) == -1:
            print('Lista vazia')
        if services.buscar_id(id, dados.lista_todos_usuarios) == None:
            print('Usuário não encontrado')
        print(*services.buscar_id(id, dados.lista_todos_usuarios).values())


        chave = input('O que deseja alterar(nome ou email): ')
        if chave not in ('nome', 'email'):
            print('Chave inválida')
        else:
            novo_valor = input('Digite o novo valor: ')
            if chave == 'nome' and not novo_valor.isalpha():
                print('Entrada inválida')
                continue
            usuario = services.buscar_id(id, dados.lista_todos_usuarios)
            services.atualizar_usuario(usuario, chave, novo_valor)
            print('Usuário atualizado com sucesso')

    elif choice == '5':
        os.system('cls')

        id = input('Digite a Id: ')
        if services.desativar_usuario(id, dados.lista_todos_usuarios)\
        == -1:
            print('Usuário não encontrado')
            continue

        print('Usuário desativado')

    elif choice == '6':
        os.system('cls')

        id = input('Digite a Id: ')
        if services.ativar_usuario(id, dados.lista_todos_usuarios)\
        == -1:
            print('Usuário não encontrado')
            continue

        print('Usuário ativado')

    elif choice == '7':
        os.system('cls')

        if services.listar_todos_usuarios(dados.lista_todos_usuarios) == -1:
            print('Lista vazia')

    elif choice == '0':
        print('Saindo...')
        break
    else:
        os.system('cls')
        
        print('\nEntrada inválida\n')