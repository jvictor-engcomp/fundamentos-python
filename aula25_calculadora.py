while True:
    numero_1 = input('Digite o número 1: ')
    numero_2 = input('Digite o número 2: ')

    operador = input('Digite o operador(+-*/): ')

    try:
        num1float = float(numero_1)
        num2float = float(numero_2)
    except:
        print('Um ou ambos os números são inválidos')
        continue
    
    if operador not in '+-*/' or len(operador) > 1:
        print('Operador inválido')
        continue

    if operador == '+':
        resultado = num1float + num2float
        print(f'Resultado: {resultado}')
    elif operador == '-':
        resultado = num1float - num2float
        print(f'Resultado: {resultado}')
    elif operador == '*':
        resultado = num1float * num2float
        print(f'Resultado: {resultado}')
    elif operador == '/':
        resultado = num1float / num2float
        print(f'Resultado: {resultado}')



    sair = input('Sair da calculadora? [S]im:').lower().startswith('s')
    if sair:
        break
    