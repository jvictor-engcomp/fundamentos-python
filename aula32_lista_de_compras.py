import os

lista_de_compras = []

running = True
while running:
    choice = input('[I]nserir [A]pagar [L]istar: ').lower()

    if len(choice) > 1:
        print('entrada invalida')
        continue
    
    if choice == 'i':
        os.system('cls')
        item = input('O que deseja inserir: ')
        lista_de_compras.append(item)

    elif choice == 'a':
        os.system('cls')
        
        if not len(lista_de_compras):
            print('Lista já está vazia')
            continue

        for indice, item in enumerate(lista_de_compras):
            print(indice, item)

        indice_apagado = input('Qual item quer apagar: ')
        try:
            indice_apagado_int = int(indice_apagado)
            lista_de_compras.pop(indice_apagado_int)
            print('Apagado com sucesso')
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif choice == 'l':
        os.system('cls')

        if not len(lista_de_compras):
            print('Lista está vazia')
            continue

        for indice, item in enumerate(lista_de_compras):
            print(indice, item)

    else:
        print('entrada invalida')
        continue