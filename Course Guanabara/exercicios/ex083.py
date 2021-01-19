# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:37:43 2018

@author: bruno
"""

#EXERCÍCIO 83 - O usuário digite uma expressão qualquer que use parênteses. Analise a expressão passada está 
#com parênteses abertos e fechados na ordem correta.

print('=' * 35)
print('Validando Expressões Matemáticas')
print('=' * 35)

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')