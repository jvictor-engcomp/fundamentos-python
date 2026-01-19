numero_str = input('Digite um número inteiro: ')
if numero_str.isdigit():
    numero_int = int(numero_str)
    paridade = 'par'
    if numero_int % 2: paridade = 'impar' 
    print(f'O numero {numero_str} é {paridade}')
else:
    print('Você não digitou um número inteiro')


hora_str = input('Agora digite a hora no seguinte modelo 1240: ')  
if hora_str.isdigit() and int(hora_str) <= 2400:
    hora_int = int(hora_str)    
    hora_int = hora_int // 100
    print(hora_int)
    if hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    else:
        print('Boa noite') 
else:
    print('Você não digitou um número inteiro')


nome = input('Por fim, digite o seu nome: ')
tamanho_nome = len(nome)
if tamanho_nome <= 4:
    print(f'{nome} é um nome curto')
elif tamanho_nome == 5 or tamanho_nome == 6:
    print(f'{nome} é um nome normal')
else:
    print(f'{nome} é um nome muito grande')


