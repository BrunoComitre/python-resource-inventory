# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:12:51 2018

@author: bruno
"""

#EXERCÍCIO 26 - Leia uma frase e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

'''f = str(input('Digite uma Frase:')).upper()

print('A letra A aparece {} vezes na frase'.format(f.count('A')))
print('A primeira letra A apareceu na posição {}'.format(f.find('A') + 1))
print('A última A apareceu na posição {}'.format(f.rfind('A') + 1))'''

#Outro Jeito

f = str(input('Digite uma Frase:')).lower()

print('A letra A aparece {} vezes na frase'.format(f.count('a')))
print('A primeira letra A apareceu na posição {}'.format(f.find('a') + 1))
print('A última A apareceu na posição {}'.format(f.rfind('a') + 1))
