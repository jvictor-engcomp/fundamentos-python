from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, nomecompleto):
        nome, *sobrenome = nomecompleto.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)
        

p1 = Pessoa('joao', 'victor', 30)
print(p1.nome_completo)
p1.nome_completo = 'Thais Gisele Victor'
print(p1.nome_completo)

print()
print(asdict(p1))
print(astuple(p1))