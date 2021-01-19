# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:41 2018

@author: bruno
"""

#EXERCÍCIO 77 - Tenha uma tupla com várias palavras (não usar acentos). Depois mostre, para cada palavra, quais são as suas vogais.

print('=' * 25)
print('Contando Vogais em Tupla')
print('=' * 25)

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa Palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
