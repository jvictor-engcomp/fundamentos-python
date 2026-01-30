class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
    def falar(self):
        print(f'Meu nome é {self._nome}, tenho {self._idade} anos.')

class Estudante(Pessoa):
    def __init__(self, nome, idade, escola):
        super().__init__(nome, idade)
        self._escola = escola 

    def falar_estudante(self):
        print(f'Meu nome é {self._nome}, tenho {self._idade} anos. Estudo na escola {self._escola}')

p1 = Pessoa('joao', 19)
a1 = Estudante('maia', 20, 'master')

a1.falar_estudante()