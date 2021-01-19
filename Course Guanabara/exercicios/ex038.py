# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 38 - Receba 2 números inteiros. Mostre o maior em relação ao outro, senão iguais.

from time import sleep

print('=' * 30)
print('Comparando os Números')
print('=' * 30)

n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))

print('Calculando a Resposta...')
sleep(1.5)

if n1 > n2:
    print('O Primeiro Número é Maior: {}'.format(n1))
    print('O Segundo Número é Menor: {}'.format(n2))
elif n2 > n1:
    print('O Segundo Número é Maior: {}'.format(n2))
    print('O Primeiro Número é Menor: {}'.format(n1))
else:
    print('Os Números {} e {} São Iguais.'.format(n1, n2))
