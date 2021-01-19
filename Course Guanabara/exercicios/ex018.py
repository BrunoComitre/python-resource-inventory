# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:03:01 2018

@author: bruno
"""

#EXERCÍCIO 18 - Leia um Ângulo e mostre o valor do Seno, Cosseno e Tangente.
 
from math import radians, sin, cos, tan

a = float(input('Digite o Ângulo que você deseja: '))

print('O Ângulo de {:.2f} tem o SENO de {:.2f}\n'
      'O Ângulo de {:.2f} tem o COSSENO de {:.2f}\n'
      'O Ângulo de {:.2f} tem o TANGENTE de {:.2f}\n'
      ''.format(a, sin(radians(a)), a, cos(radians(a)), a,tan(radians(a))))
