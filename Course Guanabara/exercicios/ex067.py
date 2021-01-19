# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:00 2018

@author: bruno
"""

#EXERCÍCIO 67 - Mostre a Tabuada de Vários Números. Pare quando for solicitado um Número Negativo.

print('=' * 20)
print('Cálculo de Tábuada')
print('=' * 20)

while True:
    num = int(input('Quer ver a Tabuada de qual valor? '))
    print('-' * 50)
    if num < 0:
        break
    for i in range (1,11):
        print (f'{num} x {i} = {num*i}')
    print('-' * 50)
print ('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
