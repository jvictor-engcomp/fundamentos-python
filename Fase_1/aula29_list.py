lista_a = [10, 20, 30, 'rato']
print(lista_a)
del lista_a[3]
print(lista_a)
lista_a.append(40)
print(lista_a)
lista_a.insert(0, 5)
print(lista_a)


lista_b = [50, 60, 70]
print(lista_b)
lista_c = lista_a + lista_b
print(lista_c)

print(lista_a)
lista_a.extend(lista_b)
print(lista_a)

lista_x = [1, 2, 3]
lista_y = lista_x

lista_x.append(4)
print(lista_y)

lista_y = lista_x.copy()
lista_x.append(5)
print(lista_x)
print(lista_y)