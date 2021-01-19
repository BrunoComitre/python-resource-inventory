# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 52 - Leia um Número Inteiro e diga se ele é ou não um Número Primo.

print('=' * 15)
print('Números Primos')
print('=' * 15)

print('Usaremos \033[1;33mAMARELO\033[m para Números Divisiveis e \033[1;31mVERMELHO\033[m para Não Divisiveis')

numero = int(input('Digite qualquer número inteiro: '))

tot = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;33m', end='')
        tot +=1
    else:
        print('\033[1;31m', end='')
    print('{} \033[m'.format(c), end='')
    
print('\nO Número {} foi dividivel {} vezes'.format(numero, tot))

if tot == 2:
    print('O Número É PRIMO')
else:
    print('O Número NÃO É PRIMO')

