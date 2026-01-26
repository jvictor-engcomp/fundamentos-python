import json
from aula57_a import caminho, Pessoa

with open(caminho, 'r', encoding= 'utf8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas)

    p1 = Pessoa(**pessoas[0])

    print(p1.nome)