from usuario_repository import UsuarioRepository, EmailSemArroba
from usuario_service import UsuarioService, EmailJaUsadoError
from pprint import pprint
repositorio = UsuarioRepository()
app = UsuarioService(repositorio)

def try_criar_usuario(nome: str, email: str) -> None:
    try:
        app.criar_usuario(nome, email)
    except EmailJaUsadoError:
        print('email já usado')
    except EmailSemArroba:
        print('email inválido')

try_criar_usuario('joao', 'jotave@gmail')
try_criar_usuario('thais', 'thais@gmail')
try_criar_usuario('viviane', 'vivi@gmail')
try_criar_usuario('leandro', 'leandro@gmail')
pprint(repositorio.listar_todos())

idteste = repositorio.lista[0].id
app.desativar(idteste)


print()
pprint(app.listar_ativos())

print()
pprint(repositorio.listar_todos())

app.ativar(idteste)

print()
pprint(app.listar_ativos())

print(app.excluir_usuario(idteste))

print()
pprint(app.listar_ativos())


# print(app.buscar_por_email('jotave@gmail'))
# print(app.buscar_por_id(123))
