# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:37:42 2018

@author: bruno
"""

#EXERCÍCIO 82 - Leia vários números e coloque na lista, cria duas listas extras que vão conter apenas pares e ímpares
#respectivamente, mostre o conteúdo das três listas geradas.

print('=' * 35)
print('Dividindo Valores em Várias Listas')
print('=' * 35)

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
