# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:12:45 2018

@author: bruno
"""

#EXERCÍCIO 23 - Leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Exemplo: Digita 1834 e mostre unidade:4, dezena:3, centena:8, milhar:1.

n = int(input('Informe um Número: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o Número {}...'.format(n))

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
