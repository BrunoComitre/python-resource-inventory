# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:02 2018

@author: bruno
"""

#EXERCÍCIO 53 - Leia uma Frase e diga se ela é um Palíndromo considerando os espaços.

print('=' * 15)
print('Palíndromo')
print('=' * 15)

frase = str(input('Digite uma Frase: ')).strip().upper()

palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
print('O Inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A Frase Digitada Não é PALÍNDROMO')
