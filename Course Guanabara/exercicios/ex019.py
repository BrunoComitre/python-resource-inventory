# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:03:03 2018

@author: bruno
"""

#EXERCÍCIO 19 - Leia Quatro nomes, e escolha um aleatório.

import random

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('O Aluno escolhifo foi: {}'.format(escolhido))
