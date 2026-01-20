def soma(a, b):
    print(f'{a=} {b=} | a + b = {a + b}')

soma(2, 3)
soma(9, 5) #não nomeado, posicional
soma(b = 3, a = 89) #nomeado

def soma2(a = 0, b = 0): #valores padrão
    print(f'{a=} {b=} | a + b = {a + b}')

soma2(2)
soma2(5) 
soma2(b = 3) 

def soma3(a, b, c = None):
    if c is None:
        print(f'{a=} {b=} | a + b = {a + b}')
    else:
        print(f'{a=} {b=} {c=} | a + b + c = {a + b + c}')

soma3(2, 4)
soma3(2, 3, 4)

def soma4(a, b):
    return a + b

variavel = soma4(1, 2)
print(soma4(1,2))
print(variavel)
