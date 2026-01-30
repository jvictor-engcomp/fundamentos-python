from typing import Optional
from random import randint
from usuario import Usuario
from usuario_repository import UsuarioRepository

class EmailJaUsadoError(Exception):
    pass
    
class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository
        self.emails_usados: set[str] = set()
        self.ids_usados: set[int] = set()
        
    def permite_email(self, email: str) -> Optional[EmailJaUsadoError]:  
        if email in self.emails_usados:
            raise EmailJaUsadoError('email já usado')
        
    def criar_usuario(self, nome: str, email: str) -> Optional[Exception]:
        # valida dados
        id = randint(0, 9999)
        while id in self.ids_usados:
            id = randint(0, 9999)
        self.permite_email(email)
        
        # cria e adiciona na lista
        usuario = Usuario(id, nome, email)
        self.repository.adicionar_na_lista(usuario)

        # adiciona aos sets
        self.ids_usados.add(id)
        self.emails_usados.add(email)

    def excluir_usuario(self, id: int) -> bool:
        usuario_a_deletar = self.buscar_por_id(id)
        if usuario_a_deletar is None:
            return False
        self.repository.excluir_da_lista(usuario_a_deletar)
        return True

    def listar_ativos(self) -> list[Usuario]:
        lista = [
            usuario
            for usuario in self.repository.lista
            if usuario.ativo
        ]
        return lista

    def buscar_por_id(self, id: int) -> Optional[Usuario]:
        for usuario in self.repository.lista:
            if usuario.id == id:
                return usuario
            
    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        for usuario in self.repository.lista:
            if usuario.email == email:
                return usuario
            
    def desativar(self, id: int) -> bool:
        usuario_a_desativar: Usuario = self.buscar_por_id(id)
        if usuario_a_desativar is None:
            return False
        return usuario_a_desativar.desativar()
        
    def ativar(self, id: int) -> bool:
        usuario_a_ativar = self.buscar_por_id(id)
        if usuario_a_ativar is None:
            return False
        return usuario_a_ativar.ativar()
    
   
    
            
            
