# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        class_name = __class__.__name__
        return f'{class_name}({self.x}, {self.y})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)


p1 = Ponto(4, 5)
p2 = Ponto(7, 9)

print(f'{p1}')
print(f'{p1!r}')
print(f'{p1!s}')

p3 = p1 + p2
print(p3)