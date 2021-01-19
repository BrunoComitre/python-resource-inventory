# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:03:06 2018

@author: bruno
"""

#EXERCÍCIO 20 - Leia quatro nomes e mostre a ordem sorteada.

import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de Apresentação será: ')
print(lista)
