class Carro:
    def __init__(self, cor, ano, preco):
        self.cor_do_carro = cor
        self.ano = ano
        self.preco = preco

    @property
    def cor(self):
        return self.cor_do_carro 
    
    @property
    def ano_do_carro(self):
        return self.ano
    
celta = Carro('Azul', 1997, 5)

print(celta.cor)
print(celta.ano_do_carro)

#transforma um atributo em um método

celta.preco = 1000
print(celta.preco)

# estudar @cor.setter