#tudo em python é um objteto. Portanto, têm métodos 
a = 'rapaz'
b = 'cachorro'
c = 2.5545648

string = 'c = {argc:.3f} a = {arga} b = {argb} c = {argc} a = {arga}'

string_formatada = string.format(arga = a, argb = b, argc = c)
print(string_formatada)