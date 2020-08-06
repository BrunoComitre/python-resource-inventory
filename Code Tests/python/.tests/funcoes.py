#
# Série sobre Funções em Python 
# https://www.youtube.com/watch?v=xR57ED4DfFY&list=PLOQgLBuj2-3LRIKxqcse1EL4hXhUFuHsR&index=1 
# 

"""
serie de funções #1
"""
def funcao_nomeada():  # toda função por conseguencia tem um retorno
    return 'Oi'

anonima = lambda : 'Oi'  # não precisa ter um nome, lambda nao precissa sser colocada em variável

class FuncaoClasse:  # usar classe como função através do dander call
    def __call__(self):
        return 'Oi'

"""
serie de funções #2
"""

anonima =  lambda param: param + 2  # definido parametro em uma função lambda
# retorna : <function __main__.<lambda>(param)>
# significa: que está na main, nosso módulo principal de execução
# que é uma lambda
# e que recebe um parametro

anonima_plus =  lambda param1, param2: param1 + param2

def soma_posicional(x, y):
    """X e Y são parametros posicionais"""
    return x + y

def soma_nomeados(x=7, y=7):
    """x e y são parametros nomeados
    na falta de X ou Y, o valor 7 será usado
    """
    print(f'x: {x},y: {y}')
    return x + y

def soma_explicitamente_nomeados(*, x=7, y=7):  # tudo que está do asterisco para trás, só pode ser chamada de maneira nomeada
    """exemplo pra editar o * passar tipo x=8, ou y=6
    para alterar, pois passando só o valor 8 ou 6 por exemplo
    não faria alteração, gera erro, pois falta o argumento posicional 
    """
    print(f'x: {x},y: {y}')
    return x + y

def soma_explicitamente_nomeados2(x=7, *, y=7):  # tudo que está do asterisco para trás, só pode ser chamada de maneira nomeada
    """como no exemplo acima, agora x pode ser possicional, pode mandar 8 ao invés de x = 8,
    mas y será sempre explicitamente nomeado, ou seja, pode alterar valor com y = 8, mas se só
    mandar 8, irá dar erro
    """
    print(f'x: {x},y: {y}')
    return x + y

def soma_explicitamente_posicionais(x, y, /):  # tudo que está da barra para trás, só pode ser chamada de maneira nomeada
    """isso funciona em python 3.8 pra frente
    se passar x = 1 e y = 2, ele reclama de ser posicional,
    se passar apenas 1 e 2 ele irá aceitar
    """
    print(f'x: {x},y: {y}')
    return x + y

def soma_tudo_mix(x, y, /, z, *, w):
    """
    x e y, como estritamente posicionais
    z, como misto
    w, como estritamente nomeado
    para funcionar precisa ser: (1, 2, 3, w=1) ou (1, 2, z=3, w=1) 
    """
    print(f'x: {x}, y: {y}, z: {z}, w: {w}')
    return x, y, z, w, sum(x, y, z, w)

"""
serie de funções #3 - Des|empacotamento de argumentos
"""

# EMPACOTAMENTO
# desse jeito você teria de passar 15 argumentos para executar a função
def meu_sum(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    return sum((a, b, c, d, e, f, g, h, i, j, k, l, m, n, o))
# com isso você pode criar argumentos (args) para facilitar

# def meu_sum(*args, **kwargs):
def meu_sum(*grupo_posicionados, **grupo_nomeado):
    print(grupo_posicionados, grupo_nomeado)
    print(type(grupo_posicionados), type(grupo_nomeado))
    return grupo_posicionados, grupo_nomeado

# DESEMPACOTAMENTO
lista = [-1, 2, 3, 4, -10]

def meu_min(a, b, c, d, *args):
    return min((a, b, c, d, *lista))

dicionario = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

def meu_max(a=0, b=0, c=0, d=0):
    return min((a, b, c, d, **dicionario))
# para desempacotar passar: meu_mix(*lista) , meu_max(**dicionario)

"""
serie de funções #4 - Anotações de Tipo
"""

# anotação padrão
def soma(x: int, y: int) -> int:
    return x + y

from difflib import ndiff
from functools import partial, reduce
# utilizando Number
from numbers import Number
from operator import add, itemgetter, mul, sub
# exemplo para se ccriar um novo tipo
# utilizando Any
# utilizando Typing
from typing import Any, Callable, Dict, List, NewType, NoReturn, Union


# este engloba o int, float, complex
def soma(x: Number, y: Number) -> Number:
    return x + y

# este engloba os de cima, int, floar, complex, mais o str, dict, list
def soma(x: Union[Number, str, list], y: Union[Number, str, list]) -> Union[Number, str, list]:
    return x + y

# ou podemos abstrair da seguinte forma

Somavel = Union[Number, str, list]

def soma(x: Somavel, y: Somavel) -> Somavel:
    return x + y

# este engloba os de cima, int, floar, complex, mais o str, dict, list
def identidade(val: Any) -> Any:
    return val

"""
serie de funções #5 - Documentação de funções
"""


Radiano = NewType('Radiano', int)

def cal_radianus_triangulo(x, y, H: list) -> Radiano:
    ...

# padronização de docstring
def soma(x, y):
    # PEP-257
    """Soma 2 tipos somáveis.
    
    ags:
        - x: Objeto somável
        - y: Objeto somável
    
    :returns: soma de dois somáveis.
    """
    ...

"""
serie de funções #6 - Funções como objeto de primeira classe
"""

func = lambda: 'Resultado da função'


calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}


def soma(x: Number, y: Number) -> Number:
    """Soma dois números."""
    return x + y


def sub(x: Number, y: Number) -> Number:
    """Subtrai dois números."""
    return x - y


def mult(x: Number, y: Number) -> Number:
    """Multiplica dois números."""
    return x * y


def div(x: Number, y: Number) -> Number:
    """Divide dois números."""
    return x / y


calc_nomeado = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div,
}


somas = [
    lambda x: x + 0,
    lambda x: x + 1,
    lambda x: x + 2
]


def soma_1(x: Number) -> Number:
    """Soma 1 a qualquer x de entrada."""
    return x + 1

"""
serie de funções #7 - Funções como objeto de ordem superior HOFs
HIGH ORDER FUNCTIONS
"""


soma_2 = lambda val: val + 2


# Twice
def reaplica(func: Callable, val: Any) -> Any:
    """Função que reaplica a função ao resultado da chamada."""
    return func(func(val))


def seleciona(op: str) -> Callable:
    """Seleciona uma função, usando seu nome."""
    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y
    }
    return ops[op]


palavras = [
    'amar', 'transar', 'falar', 'abacaxi', 'xixi', 'chute'
]

def take_cond(func, valores):
    for val in valores:
        if func(val):
            yield val
        else:
            break

"""
serie de funções #8 - Operator
"""


print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x - y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

# este exemplo é muito grande, da pra simplificar  com

print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(sub, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))

# exemplo com palavras

palavras = [
    'amar', 'transar', 'falar', 'abacaxi', 'xixi', 'chute'
]

sorted(palavras, key=itemgetter(1))

"""
serie de funções #9 - Funções Parciais
FUNCTOOLS
"""


soma_2 = partial(add, 2)
mul_2 = partial(mul, 2)

reduce(add, [1, 2, 3, 4, 5])  # Somatório
reduce(mul, [1, 2, 3, 4, 5])  # mul

somatorio = partial(reduce, add)
multiplicatio = partial(reduce, mul)
mul_2_all = partial(map, mul_2)
ordenar_1 = partial(sorted, key=itemgetter(1))

def func(b, c, d, e, database=None):
    return database, b, c, d, e

func_postgres = partial(func, database='postgres')
func_maria = partial(func, database='mariaDB')
func_mongo = partial(func, database='mongDB')

"""
serie de funções #10 - Funções Aninhadas
Funções dentro de funções
"""

def func():
    def _func():
        ...
    ...


def file_diff(file_1: str, file_2: str) -> NoReturn:
    def read_file(file: str) -> List:
        """Abre o arquivo, ignorando a linha inicial e final."""
        return [
            e.replace(',','')
            for e in open(file).readlines()[1: -1]
            ]

    content_1 = read_file(file_1)
    content_2 = read_file(file_2)

    print(''.join(ndiff(content_1, content_2)))
