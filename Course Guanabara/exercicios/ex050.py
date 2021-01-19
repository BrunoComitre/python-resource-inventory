# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 50 - Leia 6 Números inteiros. E some os Pares. Se o valor digitado for ímpar, desconsidere.

print('=' * 15)
print('Soma de Pares')
print('=' * 15)

s = 0
cont = 0

for c in range(1,7):
    t = int(input('Digite o {}º valor: '.format(c)))
    if t % 2 == 0:
        s += t
        cont += 1
print('Você informou {} Números Pares. A Soma de todos os valores solicitados é: {}'.format(cont, s))
