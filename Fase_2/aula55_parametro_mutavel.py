#situação problema:

def adicionar_clientes(nome, lista = []):
    lista.append(nome)
    return lista

lista1 = adicionar_clientes('joao')
adicionar_clientes('rato', lista1)
print(lista1)

lista2 = adicionar_clientes('rafael')
adicionar_clientes('donatelo', lista2)
print(lista2)
# lista1 e lista2 apontam para o mesmo endereço 


# da seguite maneira, uma nova lista é criada 
def adicionar_clientes(nome, lista = None):
    if lista == None:
        lista = []
    lista.append(nome)
    return lista

lista3 = adicionar_clientes('joao')
adicionar_clientes('rato', lista3)
print(lista3)

lista4 = adicionar_clientes('rafael')
adicionar_clientes('donatelo', lista4)
print(lista4)