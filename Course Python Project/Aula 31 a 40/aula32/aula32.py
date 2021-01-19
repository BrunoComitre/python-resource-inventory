# Esta aula é sobre funções - CONTINUAÇÃO

"""
Funções (def) - return - (Parte 2)
"""

"""
def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')

def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')
"""

# OBSERVAÇÃO - Qualquer código abaixo da palavra return, nâo será executada

"""
def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta Inválida')
"""

"""
def divisao(n1, n2):
    if n2 == 0:
        return
    
    return n1 / n2

divide = divisao(8, 2)

if divide:
    print(divide)
else:
    print('Conta Inválida')
"""

"""
def dumb():
    return 1

print(dumb(), type(dumb()))
"""

"""
def f(var):
    print(var)

def dumb():
    return f

var = dumb()('E colocar o meu valor aqui')

var = dumb()
print(id(var), id(f))

if var == f:
    print('var é igual a f')
else:
    print('var é diferente de f')
"""

def tuple():
    return ('Bruno', 'Alves', 'Comitre')

var = tuple()

print(var[0], type(var))
