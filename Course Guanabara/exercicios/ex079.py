# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:42 2018

@author: bruno
"""

#EXERCÍCIO 79 - O usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
#adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

print('=' * 30)
print('Valores Únicos em uma Lista')
print('=' * 30)

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar [S/N]? '))
    if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
