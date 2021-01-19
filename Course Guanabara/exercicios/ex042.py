# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:05 2018

@author: bruno
"""

#EXERCÍCIO 42 - Refaça o Desafio 35, mostrando se é Equilátero, Isósceles, Escaleno.

print('=' * 30)
print('Analisador de Triângulos')
print('=' * 30)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2 :
    if r1 == r2 == r3:
        triangulo = 'EQUILÁTERO'
    elif r1 == r2 or r1 == r3 or r2 == r3:
        triangulo = 'ISÓSCELES'
    elif r1 != r2 != r3 != r1:
        triangulo = 'ESCALENO'    
    print('Os Segmentos Acima PODEM FORMAR UM TRIÂNGULO {}!'.format(triangulo))
else:
    print('Os Segmentos Acima NÃO PODEM PODEM FORMAR UM TRIÂNGULO.')
 