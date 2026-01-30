class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('anonimo', idade)

p1 = Pessoa.criar_anonimo(19)
print(vars(p1), p1.nome, p1.idade)

# method -> self
# @classmethod -> cls
# @staticmethod -> nenhum dos dois