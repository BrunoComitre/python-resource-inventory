# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:37:45 2018

@author: bruno
"""

#EXERCÍCIO 86 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#0 [_][_][_]
#1 [_][_][_]
#2 [_][_][_]
#   0  1  2

print('=' * 20)
print('Matriz em Python')
print('=' * 20)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
