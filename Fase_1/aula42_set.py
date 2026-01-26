s1 = set() #vazio
s1 = {1,2,3, 3, 3, 5, 5, 1, 3} #com dados
#tiram repetição
#so aceita imutáveis, não aceita listas, tuplas ou set
#não tem indice
#não garantem a ordem 

#métodos

#pois não tem nenhuma forma de indexar, não usa = para
#adicionar
s1.add(('joao'))
s1.update('Luiz') #update so aceita um iterável
#s1.clear()
s1.discard('joao')



print(s1)

s2 = {1, 2, 3}
s3 = {2, 3, 4}

s4 = s2 | s3
print(s4)
s4 = s2 & s3
print(s4)
s4 = s2 - s3
print(s4)
s4 = s2 ^ s3
print(s4)