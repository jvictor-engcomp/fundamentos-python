import re

cpf = ''
while True:
    cpf = input('Digite o cpf seguindo o modelo 74682489070: ')

    cpf = re.sub(r'[^0-9]', '', cpf)

    primeiro_digito = cpf[0]
    entrada_e_repetida = primeiro_digito * len(cpf) == cpf

    if len(cpf) != 11 or entrada_e_repetida:
        print('CPF inválido')
    else:
        break

penultimo_digito_digitado = int(cpf[9])
ultimo_digito_digitado = int(cpf[10])

#print(ultimo_digito_digitado)

#penultimo digito
soma_nove_digitos = 0

nove_digitos = range(9)
for digito in nove_digitos:
    digito_cpf_int = int(cpf[digito])
    multiplicacao = digito_cpf_int * (10 - digito)
    soma_nove_digitos += multiplicacao

soma_nove_digitos *= 10
resto = soma_nove_digitos % 11

condicao = resto > 9
penultimo_digito = 0 if condicao else resto



#ultimo digito, fazendo de outra forma 

nove_digitos = cpf[0:10]

contagem_decrescente = 11
soma_nove_digitos_2 = 0
for numero in nove_digitos:
    numero_int = int(numero)
    multiplicacao = numero_int * contagem_decrescente
    soma_nove_digitos_2 += multiplicacao
    contagem_decrescente -= 1

soma_nove_digitos_2 *= 10
resto_2 = soma_nove_digitos_2 % 11

condicao_2 = resto_2 > 9
ultimo_digito = 0 if condicao_2 else resto_2

#print(ultimo_digito)

if penultimo_digito == penultimo_digito_digitado \
and ultimo_digito == ultimo_digito_digitado:
    print('O CPF digitado é válido')
else:
    print('O CPF digitado não é válido')
