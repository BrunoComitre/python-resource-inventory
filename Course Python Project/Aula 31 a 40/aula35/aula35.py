# Esta aula é sobre Expressões lambda (funções anônimas)

"""
Expressões lambda - funções anônimas
"""

# FUNÇÃO NORMAL
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2, 2)
print(var)

# UTILIZANDO LAMBDA
a = lambda x, y: x * y  # Expressão Anônima, pois nâo tem nome
print(a(2, 2))

# EXEMPLO
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort()  # Assim não funciona como exibido no print
print(lista)

# ORDENADO PELO PREÇO DO PRODUTO
def func(item):
    return item[1]

lista.sort(key=func)
print(lista)

# EXEMPLO LAMBDA
lista.sort(key=lambda item: item[1])
print(lista)

# EXEMPLO LAMBDA ORDENANDO DO MAIS CARO PARA O MAIS BARATO
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

# UTILIZANDO SORTED
print(sorted(lista, key=lambda i: i[1]))
