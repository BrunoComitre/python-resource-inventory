# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:11:52 2018

@author: bruno
"""

#EXERCÍCIO 06 - Leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input('Digite um Número:'))

print('O Dobro de {} vale: {},\n'
      'O Triplo de {} vale: {},\n'
      'A Raiz Quadrada de {} é igual a {:.2f}'.format(n,(n*2),n,(n*3),n,(n**(1/2)))) #{:.2F} Formata a raiz quadrada duas casa decimais após a vírgula.

print('Usando Raiz Quadrada {:.2f}'.format(pow(n,(1/2)))) #pow significa power n é a base e o 1/2 é o expoente, também calcula raiz quadrada.
