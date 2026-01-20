palavra_secreta = 'bombril'
palavra_cript = len(palavra_secreta) * '*'
tentativas_max = 10
tentativas = 0

while tentativas < tentativas_max:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue  
    if not letra.isalpha():
        print('O programa só aceita letras')
        continue  

    if letra in palavra_secreta:
        posicoes = ''
        indice = -1
        for ltr in palavra_secreta:
            indice += 1
            if ltr == letra:
                posicoes += str(indice)
            else:
                continue
        
        nova_palavra_cript = ''
        for i in range(len(palavra_secreta)):
            if str(i) in posicoes:
                nova_palavra_cript += letra
            elif palavra_cript[i] != '*':
                nova_palavra_cript += palavra_cript[i]
            else:
                nova_palavra_cript += '*'
        
        palavra_cript = nova_palavra_cript
        print(f'{palavra_cript}')

    else: 
        print(palavra_cript)

    if '*' not in palavra_cript:
        break

    tentativas += 1
    print(f'Tentativas restantes: {tentativas_max - tentativas}')

print('jogo acabou')