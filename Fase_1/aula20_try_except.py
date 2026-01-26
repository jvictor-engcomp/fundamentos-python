numero_str = input('digite um número: ')

if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'o dobro de {numero_str} é {numero_float * 2}')

#try:
#    numero_int = int(numero_str)
#    print(f'O dobro de {numero_str} é {numero_int * 2}')
#except:
#    print('O número escrito não é int')