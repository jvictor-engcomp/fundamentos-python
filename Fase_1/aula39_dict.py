#chave valor
pessoa = {
    'nome': 'João Victor',
    'idade': 19,
    'curso': 'engenharia de computação',
    #'salario': 1000
}

chave = 'curso'
print(pessoa[chave])

for chave in pessoa:
    print(chave, pessoa[chave])

chave_nova = 'sexo'

#del pessoa['curso']

pessoa[chave_nova] = 'masculino'
print(pessoa)

if pessoa.get('curso') is None:
    print('curso foi retirado')
else:
    print(pessoa['curso'])

#metodos
pessoa.setdefault('salario', None)
print(pessoa['salario'])

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

#get
#pop apaga e retorna o valor
#popitem apaga o ultimo
#update atualiza e cria
