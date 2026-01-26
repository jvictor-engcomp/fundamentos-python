import json

lista = []
qtd = 0
comandos = ('desfazer', 'refazer', 'listar', 'deletar', 'sair')

caminho = 'C:\\Users\\João Victor\\Desktop\\fundamentos-python\\Fase_2\\'
nome = 'aula56dados.json'
caminho += nome

try:
    with open(caminho, 'r', encoding= 'utf8') as arquivo:
        dados = json.load(arquivo)
        lista = dados['lista']
        qtd = dados['qtd']
except:
    with open(caminho, 'w', encoding= 'utf8') as arquivo:
        dados = {
            'lista': [],
            'qtd': 0,
        }
        json.dump(dados, arquivo, indent=4)
        


def desfazer():
    global qtd
    if qtd == 0: 
        print('Nada a desfazer')
        return -1
    else:
        qtd -= 1
        return 1

def refazer():
    global qtd, lista
    if len(lista) == 0:
        print('Nada a refazer')
        return - 1
    elif qtd < len(lista):
        qtd += 1
        return 1
    
def listar():
    global qtd, lista
    if len(lista) == 0:
        print('Sem tarefas')
        return - 1
    else:
        for indice, tarefa in enumerate(lista):
            if indice < qtd:
                print(tarefa)
            
    
def adicionar_tarefa(nome):
    global qtd 
    lista.insert(qtd, nome)
    qtd += 1

def deletar_ultima_atual():
    global qtd, lista
    if qtd == 0:
        print('Nada a ser deletado')
    else:
        deletado = lista.pop(qtd - 1)
        print(f'{deletado} foi deletado')
        qtd -= 1


while True:
    
    comando = input('Digite uma tarefa ou comando( desfazer, refazer, listar, deletar, sair): ')
    if comando not in comandos:
        adicionar_tarefa(comando)
    elif comando == 'desfazer':
        desfazer()
    elif comando == 'refazer':
        refazer()
    elif comando == 'listar':
        listar()
    elif comando == 'deletar':
        deletar_ultima_atual()
    elif comando == 'sair':
        break

with open(caminho, 'w', encoding= 'utf8') as arquivo:
        dados = {
            'lista': lista,
            'qtd': qtd,
        }
        json.dump(dados, arquivo, indent=4)