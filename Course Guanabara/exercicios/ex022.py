# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:12:39 2018

@author: bruno
"""

#EXERCÍCIO 22 - Leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

'''n = str(input('Digite seu Nome Completo: ')).strip()

print('Analisando seu Nome...')

print('Seu nome em maiúscula é {} '.format(n.upper()))
print('Seu nome em minúscula é {} '.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))'''

#Outro Jeito

n = str(input('Digite seu Nome Completo: ')).strip()

print('Analisando seu Nome...')

print('Seu nome em maiúscula é {} '.format(n.upper()))
print('Seu nome em minúscula é {} '.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n) - n.count(' ')))
separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
