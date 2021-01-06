"""
Documentação deste módulo

Ele não faz nada, mas é um exemplo de boas práticas
Typing - https://docs.python.org/3/library/typing.html
"""

variavel = 'Variável'
print(type(variavel))

x: int = 10
y: float = 10.5
z: str = 'Texto'
k: bool = True

def funcao(p1: float, p2: str, p3: dict):
    return p1, p2, p3

funcao('str', False, [])
funcao(10.8, 'str', {'valor':'texto'})

def teste(p1: float, p2: str, p3: dict) -> float:
    return 10.10

print(teste(10.8, 'str', {}))

from typing import Union

def exemplo() -> Union[list, dict]:
    return []
