# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:42 2018

@author: bruno
"""

#EXERCÍCIO 78 - Leia 5 valores numéricos e guarde na lista, mostre maior e o menor valor digitado e as suas respectivas posições na lista.

print('=' * 35)
print('Maior e Menor Valores na Lista')
print('=' * 35)

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c+1}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-=' * 25)
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i+1} ', end='')
print()
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i+1} ', end='')
print()
