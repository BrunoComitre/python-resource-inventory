# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:23 2018

@author: bruno
"""

#EXERCÍCIO 16 - Leia um numero real e mostre porção inteira.
#Exemplo: Digita 6.127, e exiba 6

from math import trunc

n = float(input('Digite um Valor: '))

print('O valor digitado foi {}, e a sua porção inteira é {}.'.format(n, trunc(n)))
