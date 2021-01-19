# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:02 2018

@author: bruno
"""

#EXERCÍCIO 54 - Leia Ano de Nascimento de 7 pessoas. No final mostre quantos são de maior e quantos não são de maior.

from datetime import date

print('=' * 15)
print('Maior de Idade')
print('=' * 15)

atual = date.today().year
totalmaior = 0
totalmenor = 0

for a in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(a)))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoa(s) maiore(s) de idade.'.format(totalmaior))
print('Ao todo tivemos {} pessoa(s) menore(s) de idade.'.format(totalmenor))
