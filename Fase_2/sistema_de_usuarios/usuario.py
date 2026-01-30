class EmailSemArroba(Exception):
    pass

class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id: int = id
        self.nome: str = nome
        self._email: str = ''
        self.email = email
        self._ativo: bool = True
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, valor: str) -> None:
        if '@' not in valor:
            raise EmailSemArroba('Email inválido')
        self._email = valor

    @property
    def ativo(self) -> bool:
        return self._ativo
    
    def ativar(self) -> bool:
        if self.ativo: return False
        self._ativo = True
        return True

    def desativar(self) -> bool:
        if not self.ativo: 
            return False
        self._ativo = False
        return True

    def __repr__(self):
        class_name = __class__.__name__
        return f'{class_name}(id = {self.id}, nome = {self.nome}, email = {self._email}, ativo = {self.ativo})'

