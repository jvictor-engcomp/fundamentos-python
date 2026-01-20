variavel_teste = 'a'
variavel_teste1 = 'v'
print(id(variavel_teste))
print(id(variavel_teste1))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('dentro if')
else:
    print('passou else')

if passou_no_if is not None:
    print('passou no if')
else:
    print('não passou no if')