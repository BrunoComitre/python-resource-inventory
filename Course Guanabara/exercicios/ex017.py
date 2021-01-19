# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:02:58 2018

@author: bruno
"""

#EXERCÍCIO 17 - Leia comprimento do cateto Oposto e Adjacente e calcule e mostre a Hipotenusa.

from math import hypot

o = float(input('Comprimento do Cateto Oposto: '))
a = float(input('Comprimento do Cateto Adejacente: '))
h = hypot(o, a)

print('A Hipotenusa vai medir {:.2f}'.format(h))
