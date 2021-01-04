"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse (!!!???)
"""

# class A:
#     attr = 'Valor'
    

# a = A()
# b = A()
# c = A()

######

# class Fala():
#     def fala(self):
#         self.b_fala()

# class B():
#     def b_fala(self):
#         print('Oi')

# b = B()
# b.fala()

######

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        print(namespace)
        if 'b_fala' not in namespace:
            print(f'Precisa criar um método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método e não um atributo em {name}')
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'Valor'
    b_fala = 'Teste'
    pass
    def b_fala(self):
        print('Oi')
    def teste(self):
        pass

b = B()
# b.fala()
