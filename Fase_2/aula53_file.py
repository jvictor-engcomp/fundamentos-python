import os

caminho = 'aula53.txt'

#arquivo = open(caminho, 'w')
#arquivo.close()

with open(caminho, 'w+', encoding='utf8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.seek(0, 0)
    print(arquivo.read())

    arquivo.writelines(
        ('João\n', 'Thais\n', )
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print(arquivo.read())
    print(arquivo.read())
    print(arquivo.readline().strip())



os.remove(caminho)