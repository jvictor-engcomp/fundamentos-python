# *desempacota uma tupla

# aqui o parâmetro é uma tupla descompactada
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    print(total)


#seria usado assim 
tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
lista = list(tupla)
print(lista)
soma(*lista)

#ou assim
soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#*args -> tuplas listas, argumentos não nomeados 
#**kwargs -> dicionário, argumentos nomeados

dados_1 = {
    'nome': 'joao',
    'idade': 19
}

dados_2 = {
    'cor_favorita': 'azul',
    'jogo_favorito': 'stray'
}

dados_completos = {**dados_1, **dados_2}
print(dados_completos)

#ambos parametros recebem desempacotado
def teste_args_kwargs(*args, **kwargs):
    print(args, type(args), kwargs, type(kwargs))


teste_args_kwargs(*(1,2,3), nome = 'janja', idade = 50 )
teste_args_kwargs(1, 2, 3, **dados_completos)