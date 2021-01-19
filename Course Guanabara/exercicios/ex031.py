# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:36:37 2018

@author: bruno
"""

#EXERCÍCIO 31 - Receba a distância da viagem em Km. E calcule o preço da passagem.
# Custa R$ 0,50 por Km de viagens até 200Km e R$ 0,45 para viagens mais longas.

'''v = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km'.format(v))

if v <= 200:
    p = v * 0.50
else:
    p = v * 0.45
    
print('E o preço da sua passagem será de R${:.2f}'.format(p))'''

# Outro Jeito de fazer simplificado

v = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km'.format(v))

p = v * 0.50 if v <= 200 else v * 0.45

p recebe o valor de v x 50 se v maior igual 200 senao v x45
    
print('E o preço da sua passagem será de R${:.2f}'.format(p))
