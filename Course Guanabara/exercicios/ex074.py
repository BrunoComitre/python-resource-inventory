# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:38 2018

@author: bruno
"""

#EXERCÍCIO 74 - Gere cinco números aleatórios e colocar em uma tupla, mostre a listagem de números gerados e também indique o menor e o maior.

from random import randint

print('=' * 35)
print('Maior e Menor Valores em Tupla')
print('=' * 35)

aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10),
             randint(1, 10), randint(1, 10))

print('Os Valores Sorteados Foram: ', end='')
for n in aleatorio:
    print(f'{n} ', end='')
print(f'\nO Maior Valor Sorteado Foi: {max(aleatorio)}')
print(f'O Menor Valor Sorteado Foi: {min(aleatorio)}')
