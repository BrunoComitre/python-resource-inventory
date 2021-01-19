# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:11:57 2018

@author: bruno
"""

#EXERCÍCIO 11 - Leia largura e altura de uma parede em metros. Calcule área, e quantidade de tinta.
#Sabendo cada litro de tinta pinta uma área de 2m².

lar = float(input('Digite a Largura da Parede:'))
alt = float(input('Digite a Altura da Parede:'))

print('Sua parede tem a dimensão de {:.2f} x {:.2f}, e sua área é de {:.2f}m².'.format(lar, alt, (lar*alt)))
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format((lar*alt)/2))
