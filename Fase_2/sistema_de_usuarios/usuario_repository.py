from usuario import Usuario, EmailSemArroba
from typing import Optional


class UsuarioRepository:
    def __init__(self):
        self.lista: list[Usuario] = []
    
    def adicionar_na_lista(self, usuario: Usuario) -> Optional[EmailSemArroba]:
        self.lista.append(usuario)

    def excluir_da_lista(self, usuario: Usuario) -> None:
        self.lista.remove(usuario)
    
    def listar_todos(self) -> list[Usuario]:
        return self.lista
    
    
    
    
    
            
    
            
    
    


