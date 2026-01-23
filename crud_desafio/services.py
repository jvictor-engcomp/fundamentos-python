import dados

def cabecalho():
    titulo = 'Gerenciador de Usuários'
    print(30 * '-')
    print(f'{titulo:-^30}')
    print(30 * '-')

def opcoes():
    print('1 - Criar usuário')
    print('2 - Listar usuários ativos')
    print('3 - Buscar usuário por ID')
    print('4 - Atualizar usuário')
    print('5 - Desativar usuário')
    print('6 - Ativar usuário')
    print('7 - Listar todos usuários')
    print('0 - Sair')

def criar_usuario(id, nome, email, status = True):
    if email in dados.emails_cadastrados:
        return None
    if id in dados.ids_cadastrados:
        return None
    pessoa = {
        'id': id,
        'nome': nome,
        'email': email,
        'status': status
    }
    dados.lista_todos_usuarios.append(pessoa)
    dados.emails_cadastrados.add(email)
    dados.ids_cadastrados.add(id)
    return pessoa

def listar_todos_usuarios(lista):
    if len(lista) == 0:
        return -1
    lista_enumerada = enumerate(lista)
    for indice, usuario in lista_enumerada:
        print(indice, *usuario.values(), sep = '  ')

def listar_usuarios_ativos(lista):
    if len(lista) == 0:
        return -1
    lista_enumerada = enumerate(lista)
    for indice, usuario in lista_enumerada:
        if usuario['status'] == True:
            print(indice, *usuario.values(), sep = '  ')

def buscar_id(id, lista):
    if len(lista) == 0:
        return -1
    for usuario in lista:
        if id == usuario['id']:
            return usuario
    return None

def atualizar_usuario(usuario, chave, novo_valor):
    if chave == 'id':
        return -1
    usuario[chave] = novo_valor
    

def desativar_usuario(id, lista):
    usuario = buscar_id(id,lista)
    if usuario is not None and usuario != -1:
        usuario['status'] = False
    else:
        return -1
    
def ativar_usuario(id, lista):
    usuario = buscar_id(id,lista)
    if usuario is not None and usuario != -1:
        usuario['status'] = True
    else:
        return -1


if __name__ == '__main__':
    criar_usuario('123', 'joao', 'jotave1@gmail.com')
    criar_usuario('456', 'joao', 'jotave2@gmail.com')
    criar_usuario('789', 'joao', 'jotave3@gmail.com')
    criar_usuario('159', 'joao', 'jotave4@gmail.com')

    listar_todos_usuarios(dados.lista_todos_usuarios)

    usuario = buscar_id('456', dados.lista_todos_usuarios)
    if usuario is not None:
        print(*usuario.values())

    desativar_usuario('456', dados.lista_todos_usuarios)

    listar_todos_usuarios(dados.lista_todos_usuarios)

    listar_usuarios_ativos(dados.lista_todos_usuarios)