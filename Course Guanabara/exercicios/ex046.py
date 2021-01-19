# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:04 2018

@author: bruno
"""

#EXERCÍCIO 46 - Contagem Regressiva de Fogos de 10 até 0 com 1 segundo de pausa entre eles.

from time import sleep

print('=' * 20)
print('Contagem Regressiva')
print('=' * 20)

for c in range (10, -1, -1):
    print(c)
    sleep(1)
    
print('BOOM BOOM POOW')
