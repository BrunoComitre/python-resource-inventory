# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:11:56 2018

@author: bruno
"""

#EXERCÍCIO 12 - Leia o preço de um produto e mostre seu preço com 5% de desconto.

'''p = float(input('Qual o preço do Produto? R$ '))

print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(p, p*0.95))'''#formas de aplicar porcentagem

#Outra forma de aplicar porcentagem

'''p = float(input('Qual o preço do Produto? R$ '))
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(p, p-(p*5/100)))'''

#Outro jeito de se fazer o Cálculo

p = float(input('Qual o valor atual do produto? R$ '))
d = float(input('Deseja dar quanto % de desconto? '))

print('O produto que custava R$ {:.2f} teve um desconto de {:.2f}% agora custa R$ {:.2f}\n'
      'Quanto foi descontado: {:.2f}'
      ''.format(p, d, p -(p *(d/100)), (p*(d/100))))
