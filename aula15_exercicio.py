primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segunfo valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro valor = {primeiro_valor} é maior que o segundo valor = {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'primeiro valor é igual ao segundo valor')
else:
    print(f'segundo valor = {segundo_valor} é maior que o primeiro valor = {primeiro_valor}')
    