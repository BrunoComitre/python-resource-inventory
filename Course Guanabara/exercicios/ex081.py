# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:37:41 2018

@author: bruno
"""

#EXERCÍCIO 81 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se valor 5 foi digitado, está ou não na lista.

print('=' * 30)
print('Extraindo Dados de uma Lista')
print('=' * 30)

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
    