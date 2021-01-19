# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:01 2018

@author: bruno
"""

#EXERCÍCIO 60 - Leia um número e mostre o seu fatorial.

print('=' * 20)
print('Fatorial em Python')
print('=' * 20)

f = int(input('Digite um Número para calcular o seu Fatorial (n!): '))
fat = 1

print('O Fatorial de {}! ='.format(f),end=' ')
while f > 0:
    fat *= f
    print('{}'.format(f),'x' if f > 1 else '=',end=' ')
    f -= 1
print('{}'.format(fat))
