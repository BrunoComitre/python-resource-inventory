# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:41 2018

@author: bruno
"""

#EXERCÍCIO 76 - Tenha uma tupla única de produtos e preços, na sequência, mostre uma listagem de preços, organizando os dados em forma tabular.

print('=' * 30)
print('Lista de Preços com Tupla')
print('=' * 30)

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
