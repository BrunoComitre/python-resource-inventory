# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:04 2018

@author: bruno
"""

#EXERCÍCIO 48 - Calcule a soma de todos os ímpares que são múltiplos de 3 no intervalo de 1 até 500.

print('=' * 20)
print('Soma dos Ímpares')
print('=' * 20)

s = 0
cont = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            cont = cont + 1
            s += c
print('A Soma de todos os {} valores solicitados é: {}'.format(cont, s))
