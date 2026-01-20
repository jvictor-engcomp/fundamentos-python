frase = 'python e uma linguagem muito interessante'\
'e estou aprendendo para poder atuar em beckend com fastapi'

letra_maior = frase[0]

for letra in frase:
    if frase.count(letra) > frase.count(letra_maior) and letra != ' ':
        print(f'{letra}')
        letra_maior = letra
    else:
        print(f'{letra}')
print(f'Letra que mais aparece: {letra_maior}{frase.count(letra_maior)}')