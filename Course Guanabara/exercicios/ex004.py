# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:28:03 2018

@author: bruno
"""

#EXERCÍCIO 04 - Leia algo pelo teclado, e mostre na tela o tipo primitivo e todas as informações possíveis.

valor = input('Digite algo: ')

print('O tipo primitivo desse valor "{}" é: {}'.format(valor, type(valor)))
print('"{}" Só tem Espaço? {}'.format(valor, valor.isspace()))
print('"{}" É um Número? {}'.format(valor, valor.isnumeric()))
print('"{}" É Alfabético? {}'.format(valor, valor.isalpha()))
print('"{}" É Alfanumérico? {}'.format(valor, valor.isalnum()))
print('"{}" Está em Maiúsculas? {}'.format(valor, valor.isupper()))
print('"{}" Está em Minúsculas? {}'.format(valor, valor.islower()))
print('"{}" Está Captalizado? {}\n'.format(valor, valor.istitle()))

#De um Outro Jeito
    
print('Ele é um numero:{}\n'
      'Ele é alpha numerico:{}\n'
      'Ele é somente alpha:{}\n'
      'Ele é constituido inteiramente por letras maiusculas:{}\n'
      'Ele é constituido inteiramente por letras minusculas:{}\n'
      'Ele esta captalisado:{}'
      ''.format(valor.isnumeric(),valor.isalpha(),valor.isalpha(),valor.isupper(),valor.islower(),valor.istitle()))    