# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:12:51 2018

@author: bruno
"""

#EXERCÍCIO 27 - Leia o nome completo de uma pessoa. Mostre em seguida o primeiro e o último nome separadamente.
#Exemplo: Bruno Alves Comitre. Primeiro: Bruno. Último: Comitre.

n = str(input('Digite seu nome Completo: ')).strip() # O strip elimina os espaços antes e depois

nome = n.split() #O split fatia o nome separado por espaços

print('Muito Prazer em te conhecer!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
