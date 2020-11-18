import sys
import time
from difflib import ndiff
from numbers import Number
from functools import partial, reduce
from typing import List, NewType, NoReturn


def file_diff(file: str) -> NoReturn:
    def read_file(file: str) -> List:
        """Abre o arquivo, ignorando a linha inicial e final."""
        return [
            e.replace(',','')
            for e in open(file).readlines()[1:]
            ]

    content = read_file(file)
    lista = [x for x in range(len(content))]

    # print(''.join(content_1))
    print(f'TAMANHO :: {sys.getsizeof(lista)}')
    print(f'TIPO :: {type(lista)}')


print(f'DEZ ITENS ::')
print(file_diff('dez_itens.txt'))
print()

print(f'CEM ITENS ::')
print(file_diff('cem_itens.txt'))
print()

print(f'MIL ITENS ::')
print(file_diff('um_mil.txt'))
print()

print(f'CINCO MIL ITENS ::')
print(file_diff('cinco_mil.txt'))
print()

print(f'QUINZE MIL ITENS ::')
print(file_diff('quinze_mil.txt'))
print()

print(f'QUATORZE MILHÕES ITENS ::')
print(file_diff('quatorze_milhoes.txt'))
print()
