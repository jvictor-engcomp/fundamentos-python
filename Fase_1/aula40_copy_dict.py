import copy

pessoa1 = {
    'nome': 'João Victor',
    'idade': 19,
    'curso': 'engenharia de computação',
    'salas': [1, 2, 3]
}

#apontam para o mesmo dicionário
#pessoa2 = pessoa1
#pessoa2['nome'] = 'thais'
#print(pessoa1)

#shallow copy, não copia mutáveis, os dois dicionários
#apontam para a mesma lista
#pessoa2 = pessoa1.copy()
#pessoa2['nome'] = 'thais'
#pessoa2['salas'][0] = 1000 
#print(pessoa1)

#copia e não aponta nada do outro 
pessoa2 = copy.deepcopy(pessoa1)
pessoa2['nome'] = 'thais'
pessoa2['salas'][0] = 1000 
print(pessoa1)