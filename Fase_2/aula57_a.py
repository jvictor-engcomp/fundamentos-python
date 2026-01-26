import json
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

nome = 'aula57.json'
caminho = 'C:\\Users\\João Victor\\Desktop\\fundamentos-python\\Fase_2\\' + nome

if __name__ == '__main__':
    p1 = Pessoa('André', 19)
    p2 = Pessoa('Rafael', 19)
    p3 = Pessoa('Leandro', 40)

    print(p1)

    lista = []
    lista.append(vars(p1))
    lista.append(vars(p2))
    lista.append(vars(p3))

    with open(caminho, 'w', encoding= 'utf8') as arquivo:
        json.dump(lista, arquivo, indent= 4)