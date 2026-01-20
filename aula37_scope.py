x = 1
y = 2
def escopo():
    global x #altera a variavel fora do escopo

    y = 20
    print(y)

    def escopo3():
        global y
        y = 30
        print(y)
    escopo3()

    x = 10
    print(x,y)

def escopo2():
    global x

    x = 11
    print(x)

print(x, y)
escopo()
print(x, y)
escopo2()
print(x)