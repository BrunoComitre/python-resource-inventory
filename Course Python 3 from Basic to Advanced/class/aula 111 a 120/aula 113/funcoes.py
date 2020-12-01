"""
Descrição rápida e simples

Esta é uma descrição de
documentação de funções em Python

Documentação referente ao módulo
"""

variavel1 = 'Valor 1'

def funcao(x, y):
    """Documentação da função"""
    return 1

def soma(x, y):
    """Soma x e y"""
    return x + y

def multiplicacao(x, y, z=None):
    """Multiplica x, y,z

    Args:
        x ([int]): [valor]
        y ([int]): [valor]
        z ([int], optional): [valor]. Defaults to None.
    
    Multiplica x, y e z. O programador por omitir a variável z no caso não tenha
    necessidade de usá-la.
    """
    
    if z:
        return x * y
    else:
        return x * y * z

variavel2 = 'Valor 2'
variavel3 = 'Valor 3'
variavel4 = 'Valor 4'
