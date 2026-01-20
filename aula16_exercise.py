senha = '12345'

entrada = input('[E]ntrar [S]air: ')
if entrada == 'E' or entrada == 'e' :
    senha_digitada = input('Senha: ') or 'sem senha'
    print(senha_digitada)
    if senha_digitada == senha :
        print('entrar')
    else: 
        print('senha invalida')
        print('sair')
else: print('sair')