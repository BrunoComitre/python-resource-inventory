A = type(
    'A', 
    (),
    {'attr': 'Hello World!'}
    )

a = A()
print(a.attr)
print(type(a))

#####

class Principal:
    nome = 'Teste'
    
B = type(
    'B', 
    (Principal,),
    {'attr': 'Hello World!'}
    )

b = B()
print(b.attr)
print(b.nome)
print(type(b))
