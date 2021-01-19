# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:11:54 2018

@author: bruno
"""

#EXERCÍCIO 13 - Leia salário e mostre com 15% de aumento.

'''s = float(input('Qual é o Salário de Funcionário? R$ '))

print('Um Funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(s, (s*1.15)))'''

#Outra forma de aplicar porcentagem

'''s = float(input('Qual é o Salário de Funcionário? R$ '))

print('Um Funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(s, s+(s*15/100)))'''

#Outro jeito de se fazer o Cálculo

s = float(input('Qual é o Salário de Funcionário? R$ '))
a = float(input('Deseja dar quanto % de Aumento? '))

print('O Salário que era de R$ {:.2f} teve um aumento de {:.2f}%,\n'
      'O Salário atual é de R$ {:.2f}\n'
      'Houve um Aumento de R$ {:.2f}'
      ''.format(s, a, s +(s *(a/100)), (s*(a/100))))
