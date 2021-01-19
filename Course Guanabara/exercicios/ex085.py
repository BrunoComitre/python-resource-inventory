# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:37:45 2018

@author: bruno
"""

#EXERCÍCIO 85 - O usuário digita sete valores e cadastra em lista única que mantem separado por par e ímpar, mostre em ordem crescente.

print('=' * 30)
print('Listas com Pares e Ímpares')
print('=' * 30)

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
