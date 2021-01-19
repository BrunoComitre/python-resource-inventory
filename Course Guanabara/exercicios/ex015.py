# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:26:36 2018

@author: bruno
"""

#EXERCÍCIO 15 - Leia Dias e Km e mostre valor a pagar.

d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km Rodados? '))

p = (d * 60) + (k * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(p))
     