# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 49 - Como no Exercício 9. Faça a Tabuada usando o laço For.

print('=' * 10)
print('Tabuada')
print('=' * 10)

t = int(input('Digite um numero para saber a Tabuada: '))

for c in range(11):
    print('{} x {} = {}'.format(t, c, (t*c)))

# Outro Jeito de Se Fazer
 
'''print('TABUADA DE 1 A 10:')
for a in range(1, 11):
    print('--' *6)
    for b in range(1, 11):
        print('{:2} x {:2} = {:2}'.format(a, b, a*b))'''
