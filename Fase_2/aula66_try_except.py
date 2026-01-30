
try:
    a = 'a'
    b = 0 
    c = a / b
except ZeroDivisionError:
    print('erro de divisão')
except NameError as error: 
    print('erro de nomeação')
    print('nome: ', error.__class__.__name__)
finally:
    print('sempre executa')
print('pos erro')