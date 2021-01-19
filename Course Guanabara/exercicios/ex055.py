# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:02 2018

@author: bruno
"""

#EXERCÍCIO 55 - Leia o Peso de 5 Pessoas. No final mostre qual foi o maior e qual foi o menor.

print('=' * 20)
print('Peso das Pessoas')
print('=' * 20)

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o Peso da {}º Pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
            
print('O maior peso lido foi {:.2f}kg'.format(maior))
print('O menor peso lido foi {:.2f}kg'.format(menor))

# Outro Jeito de Se Fazer

'''lpesos = []
for c in range(1, 6):
    peso = float(input('Digite o Peso da {}º Pessoa: '.format(c)))
    lpesos.append(peso)
lpesos.sort()

print('O maior peso lido foi {:.2f}kg'.format(lpesos[4]))
print('O menor peso lido foi {:.2f}kg'.format(lpesos[0]))'''
