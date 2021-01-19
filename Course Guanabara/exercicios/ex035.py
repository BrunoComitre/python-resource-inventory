# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:36:38 2018

@author: bruno
"""

#EXERCÍCIO 35 - Leia o comprimento de três retas e diga se eles podem ou não formar um Triângulo.

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os Segmentos acima PODEM FORMAR Triângulo')
else:
    print('Os Segmentos acima NÃO PODEM FORMAR Triângulo')
