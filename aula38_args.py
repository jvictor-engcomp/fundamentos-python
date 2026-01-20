# *desempacota uma tupla

# aqui o parâmetro é uma tupla descompactada
def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total)


#seria usado assim 
tupla = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
soma(*tupla)

#ou assim
soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)