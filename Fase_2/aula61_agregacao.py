class Carrinho:
    def __init__(self):
        self._produtos = []

    def valor_total(self):
        total = [produto.preco for produto in self._produtos]
        return sum(total)
    
    def listar(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir(self, *produtos): #aqui *produtos fara uma tupla com os objetos: (p1, p2, ...)
        for produto in produtos:
            self._produtos.append(produto)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


meu_carrinho = Carrinho()
p1 = Produto('arroz', 5)
p2 = Produto('iogurte', 10)

meu_carrinho.inserir(p1, p2)
meu_carrinho.listar()
print(meu_carrinho.valor_total())

#situação de agregação, carrinho agrega produtos