# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:36:38 2018

@author: bruno
"""

#EXERCÍCIO 33 - Leia três números e mostre qual é o Maior e qual é o Menor.

'''n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segunto Valor: '))
n3 = int(input('Terceiro Valor: '))

#Verificando quem é Menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é Maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O Menor valor digitado foi {}'.format(menor))
print('O Maior valor digitado foi {}'.format(maior))'''

#Outro Jeito

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segunto Valor: '))
n3 = int(input('Terceiro Valor: '))

n = [n1, n2, n3]

print('O Menor valor digitado foi {}'.format(min(n)))
print('O Maior valor digitado foi {}'.format(max(n)))
