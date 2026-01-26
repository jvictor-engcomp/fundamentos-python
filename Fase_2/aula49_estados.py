class Camera:
    def __init__(self, nome, filmando = False, fotografando = False):
        self.nome = nome
        self.filmando = filmando
        self.fotografando = fotografando

    def filmar(self):
        if self.filmando == True:
            print(f'{self.nome} já está filmando')
        elif self.fotografando == True:
            print(f'Não é possífel filmar, {self.nome} está fotografando')
        else:
            print(f'{self.nome} começou a filmar')    
            self.filmando = True

    def fotografar(self):
        if self.filmando == True:
            print(f'Não é possífel fotografar, {self.nome} está filmando')
        elif self.fotografando == True:
            print(f'{self.nome} já está fotografando')
        else:
            print(f'{self.nome} começou a fotografar')    
            self.fotografando = True

    def parar_filmar(self):
        if self.filmando == False:
            print(f'{self.nome} já não está filmando')
        else:
            self.filmando = False
            print(f'{self.nome} parou de filmar')

    def parar_fotografar(self):
        if self.fotografando == False:
            print(f'{self.nome} já não está fotografando')
        else:
            self.fotografando = False
            print(f'{self.nome} parou de fotografando')       

canon = Camera('canon')
sony = Camera('sony')

sony.fotografar()
sony.filmar()
sony.parar_fotografar()
sony.filmar()

