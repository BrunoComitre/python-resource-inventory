lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))  # para saber se o meu objeto é iterável

print(hasattr(lista, '__next__'))  # para saber se um iterador

lista = iter(lista)
print(hasattr(lista, '__next__'))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))


import sys

lista2 = (list(range(10)))
print(lista2)

print(sys.getsizeof(lista2))  # pegando quandos bytes de memória ela está consumindo do computador
print(sys.getsizeof(lista))


import time

def gera():
    r = []
    for n in range(10):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()
print(f' Resultado : {v for v in g}')

for v in g:
    print(v)


def gerador():
    for n in range(10 ):
        yield n
        time.sleep(0.1)

ge = gerador()
print(ge)

print(f' Resultado : {v for v in ge}')

for v in ge:
    print(v)
    
print(hasattr(ge, '__iter__'))
print(hasattr(ge, '__next__'))
print(sys.getsizeof(ge))


lista3 = [x for x in range(100)]
print(sys.getsizeof(lista3))
print(type(lista3))
lista4 = (x for x in range(100))
print(sys.getsizeof(lista4))
print(type(lista4))
lista5 = [x for x in range(1000)]
print(sys.getsizeof(lista5))
print(type(lista5))
lista6 = (x for x in range(1000))
print(sys.getsizeof(lista6))
print(type(lista6))
lista7 = [x for x in range(10000)]
print(sys.getsizeof(lista7))
print(type(lista7))
lista8 = (x for x in range(10000))
print(sys.getsizeof(lista8))
print(type(lista8))
