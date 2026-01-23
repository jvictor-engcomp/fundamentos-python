import os

perguntas = [
    {
        'pergunta': 'Quem descobriu o Brasil?',
        'opcoes': ['Rafael Maia', 'Tom Cruise', 'Pedro Álvares Cabral', 'Cristovão Colombo'],
        'resposta': 'Pedro Álvares Cabral',
    },
    {
        'pergunta': '2 + 2?',
        'opcoes': ['3', '4', '6', '0'],
        'resposta': '4',
    },
    {
        'pergunta': '2 + 4?',
        'opcoes': ['3', '4', '6', '0'],
        'resposta': '6',
    }
]

qtd_questoes = len(perguntas)
qtd_acertadas = 0 
for questao in perguntas:
    print(questao['pergunta'])

    for indice, opcao in enumerate(questao['opcoes']):
        print(f'{indice}) {opcao}')

    i_respondido = input()
    if not i_respondido.isdigit() and ( int(i_respondido) < 0 or int(i_respondido) > 3):
        print('Resposta inválida')
        continue
    i_respondido = int(i_respondido)

    if questao['opcoes'][i_respondido] == questao['resposta']:
        print('ACERTOU!!!\n')
        qtd_acertadas += 1
    else:
        print('ERROU!!!\n')
    
    #os.system('cls')

print(f'Você acertou {qtd_acertadas} de {qtd_questoes}')