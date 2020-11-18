"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __sub__(self, other):
        novo_x = self.x - other.x
        novo_y = self.y - other.y
        return Retangulo(novo_x, novo_y)
    
    def __mul__(self, other):
        novo_x = self.x * other.x
        novo_y = self.y * other.y
        return Retangulo(novo_x, novo_y)
    
    def __div__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 / a2:
            return True
        else:
            return False
    
    def __floordiv__(self, other):
        novo_x = self.x // other.x
        novo_y = self.y // other.y
        return Retangulo(novo_x, novo_y)
    
    def __mod__(self, other):
        novo_x = self.x % other.x
        novo_y = self.y % other.y
        return Retangulo(novo_x, novo_y)
    
    def __pow__(self, other):
        novo_x = self.x ** other.x
        novo_y = self.y ** other.y
        return Retangulo(novo_x, novo_y)
    
    def __pos__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
    
    def __neg__(self, other):
        novo_x = self.x - other.x
        novo_y = self.y - other.y
        return Retangulo(novo_x, novo_y)
    
    def __le__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 <= a2:
            return True
        else:
            return False
        
    def __ge__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 >= a2:
            return True
        else:
            return False
        
    def __ne__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 != a2:
            return True
        else:
            return False
        
    def __lshift__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 << a2:
            return True
        else:
            return False
        
    def __rshift__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 >> a2:
            return True
        else:
            return False
        
    def __and__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 & a2:
            return True
        else:
            return False
        
    def __or__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 | a2:
            return True
        else:
            return False
        
    def __xor__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 ^ a2:
            return True
        else:
            return False
        
    # def __inv__(self, other):
    #     novo_x = self.x ~ other.x
    #     novo_y = self.y ~ other.y
    #     return Retangulo(novo_x, novo_y)
        
r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2

print(r1 + r3)
print(r1 - r3)
print(r1 * r3)
# print(r1 / r3)
print(r1 // r3)
print(r1 % r3)
print(r1 ** r3)
print(r1 + r3)
print(r1 - r3)
print(r1 < r3)
print(r1 > r3)
print(r1 <= r3)
print(r1 >= r3)
print(r1 == r3)
print(r1 != r3)
print(r1 << r3)
print(r1 >> r3)
print(r1 & r3)
print(r1 | r3)
print(r1 ^ r3)
# print(r1 ~ r3)
