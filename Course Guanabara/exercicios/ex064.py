# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:00 2018

@author: bruno
"""

#EXERCÍCIO 64 - Leia vários números inteiros, pare ao digitar 999. No final mostre total dos digitados e a soma, desconsiderando o Flag.

print('=' * 20)
print('Soma de Valores')
print('=' * 20)

valor = 0
cont = 0
while (True):
    n = int ( input ('Digite um Número [999 para parar]: '))
    if (n == 999):
        print ('Você digitou {} Número(s) e a soma entre eles foi {}.'.format(cont,valor))
        break
    valor += n
    cont += 1
