# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:01 2018

@author: bruno
"""

#EXERCÍCIO 61 - Como no Exercício 51. Receba a Progressão Aritmética usando a estrutura While.

print('=' * 25)
print('Progressão Aritmética')
print('=' * 25)

num = int(input('Primeiro Termo: '))
razao = int(input('Razão da Progressão Aritmética: '))
termo = num
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')   
    termo += razao
    cont += 1
print('FIM')
