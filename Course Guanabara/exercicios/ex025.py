# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:12:50 2018

@author: bruno
"""

#EXERCÍCIO 25 - Leia o nome da pessoa e diga se tem "SILVA".

'''n = str(input('Qual o seu Nome Completo? ')).strip()

print('O seu nome tem Silva? {}'.format('SILVA' in n.upper()))'''

#Outro Jeito

n = str(input('Qual o seu Nome Completo? ')).strip()

print('O seu nome tem Silva? {}'.format('silva' in n.lower()))
