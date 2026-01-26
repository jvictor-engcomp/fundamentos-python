
import random

nove_digitos = ''
while True:
    for i in range(9):
        nove_digitos += str(random.randint(0,9))


    primeiro_digito = nove_digitos[0]
    entrada_e_repetida = primeiro_digito * 9 == nove_digitos

    if entrada_e_repetida:
        continue
    else:
        break




#penultimo digito
soma_nove_digitos = 0

for i in range(9):
    digito_cpf_int = int(nove_digitos[i])
    multiplicacao = digito_cpf_int * (10 - i)
    soma_nove_digitos += multiplicacao

soma_nove_digitos *= 10
resto = soma_nove_digitos % 11

condicao = resto > 9
penultimo_digito = 0 if condicao else resto



#ultimo digito, fazendo de outra forma 
contagem_decrescente = 11
soma_nove_digitos_2 = 0
for numero in nove_digitos + str(penultimo_digito):
    numero_int = int(numero)
    multiplicacao = numero_int * contagem_decrescente
    soma_nove_digitos_2 += multiplicacao
    contagem_decrescente -= 1

soma_nove_digitos_2 *= 10
resto_2 = soma_nove_digitos_2 % 11

condicao_2 = resto_2 > 9
ultimo_digito = 0 if condicao_2 else resto_2

print(f'CPF GERADO: {nove_digitos}{penultimo_digito}{ultimo_digito}')
