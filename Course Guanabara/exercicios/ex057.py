# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:02 2018

@author: bruno
"""

#EXERCÍCIO 57 - Leia o sexo da pessoa. Só aceira M e F caso digite errado, peça para digitar novamente até o valor correto. 

print('=' * 20)
print('Sexo das Pessoas')
print('=' * 20)

sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digitou errado, por favor, informe [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso:'.format(sexo))
