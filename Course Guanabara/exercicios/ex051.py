# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 51 - Leia o Primeiro Termo e a Razão de uma Progressão Aritmética. No final mostre os 10 Primeiros termos dessa progressão.

print('=' * 25)
print('Progressão Aritmética')
print('=' * 25)

primeiro = int(input('Digite o Primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a Razão da Progressão Aritmética: '))

for c in range(1,11):
    pa = primeiro + (c - 1) * razao
    print(pa, end=' → ' )

print('Acabou')
