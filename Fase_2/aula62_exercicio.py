class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self._catalogo = []

    @property
    def catalogo(self):
        return self._catalogo
    
    @catalogo.setter
    def catalogo(self, carro):
        if not isinstance(carro, Carro):
            print('Carro não existe ')
        self._catalogo.append(carro)


    def excluir_carro_do_catalogo(self, nome):
        for indice, nome_carro in enumerate(self.catalogo):
            if nome_carro == nome:
                return self._catalogo.pop(indice)

    # def inserir_carro(self, *carros):
    #     self.carros.extend(carros)
    # def listar_carros(self):
    #     for carro in self.carros:
    #         print(carro.nome, carro.motor.tipo, carro.motor.potencia)


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        if not isinstance(motor, Motor):
            print('motor não criado')
            return
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        if not isinstance(fabricante, Fabricante):
            raise TypeError("fabricante deve ser um Fabricante")
        self._fabricante = fabricante
        fabricante._catalogo.append(self)



class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia


v8 = Motor('v8', 400)
v10 = Motor('v10', 700)
v12 = Motor('v12', 900)
    
fiat = Fabricante('Fiat')

cronos = Carro('Cronos')
palio = Carro('Palio')
toro = Carro('Toro')

byd = Carro('byd')
cronos.fabricante = fiat


palio.fabricante = fiat
palio.motor = v8

toro.fabricante = fiat

for carro in fiat.catalogo:
    print(carro.nome)
