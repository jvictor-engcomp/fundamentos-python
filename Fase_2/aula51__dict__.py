teste = {
    'nome': 'joao',
    'idade': 19
}

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa(**teste)

print(p1.nome, p1.idade)

print(p1.__dict__)
print(vars(p1))
        