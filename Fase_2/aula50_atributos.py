class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_de_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('joao', 19)
p1_ano_de_nascimento = p1.get_ano_de_nascimento()
print(p1_ano_de_nascimento)