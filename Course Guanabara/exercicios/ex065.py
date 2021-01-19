# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:00 2018

@author: bruno
"""

#EXERCÍCIO 65 - Receba vários números. No final mostre a média, menor e o maior. E pergunte se deseja ou não continuar digitar os valores.

print('=' * 20)
print('Cálculo dos Valores')
print('=' * 20)

soma = quant = media = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um Número: '))
    resp = str(input('Quer Continuar? [S/N]: ')).upper()
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você digitou {} Número(s) e a Média foi {:.2f}.'.format(quant, soma / quant))
print('O MAIOR Valor foi {} e o MENOR Valor foi {}.'.format(maior, menor))
