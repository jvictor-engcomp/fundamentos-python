lista = ['otavio', 'ruan', 'maurino', 'otavio', 'mauricio']
_, _, nome2, *_ = lista
print(nome2)

tupla = 'otavio', 'ruan', 'maurino', 'otavio', 'mauricio'
print(tupla[1])

lista_enumerada = enumerate(lista)
for item in lista_enumerada:
    print(item)

#já consumiu o enumerate
for item in lista_enumerada:
    print(item)

for indice, nome in enumerate(tupla):
    print(indice * 2, nome)


print(list(tupla))