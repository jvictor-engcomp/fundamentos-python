#import sys
#print(sys.platform)

#from sys import exit, platform
#assim não prescisa do namespace
#platform = 'AMINHA'#cuidado, sobrescreveu o import
#print(platform)
#exit()

#import sys as s
#não recomendo muito
#sys = 'alguma coisa'
#print(s.platform)
#s.exit()

from sys import *
#pior forma
#exit()

print(platform)

import aula45_modulo
from aula45_modulo import soma

aula45_modulo.soma(1,2,3,4,5)
soma(2, 3, 4, 5, 6, 7, 8, 9, 1)

import importlib

importlib.reload(aula45_modulo)#recarrega o módulo

from aula45_package import moduloaula45

moduloaula45.subtracao(1, 2, 3, 4)

if __name__ == '__main__':
    print('esta é a main')