contador = 0

while contador <= 100:
    contador += 1
    if  not contador % 2: continue
    #print(contador)

n_linhas = 0
n_colunas = 0

while n_linhas < 9:
    n_colunas = 0
    while n_colunas < 5:
        print(f'{n_linhas}{n_colunas} ', end = '')
        n_colunas += 1
    n_linhas += 1
    print()