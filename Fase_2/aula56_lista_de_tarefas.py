lista = []
qtd = 0
comandos = ('desfazer', 'refazer', 'listar', 'deletar')

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
    
    comando = input('Digite uma tarefa ou comando( desfazer, refazer, listar, deletar): ')
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