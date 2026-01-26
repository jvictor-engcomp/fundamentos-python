class Carro: #molde
    def __init__(self, nome = 'Não informado'):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

#objetos 
fusca = Carro('Fusca')
celta = Carro('Celta')

fusca.acelerar()
celta.acelerar()

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self, *args, **kwargs):
        return f'{self.nome} está comendo {(*args, *kwargs.values())}'
        
comidas = {
    'laticinio': 'leite',
    'mistura': 'frango'
}

leao = Animal('leao')
print(leao.comer('maçã', carne = 'picanha', *('cheiro verde', 'coentro'), **comidas))