#PascalCase

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('João', 'Victor')


print(p1.nome)
print(p1.sobrenome)