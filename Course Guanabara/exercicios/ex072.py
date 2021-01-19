# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:33 2018

@author: bruno
"""

#EXERCÍCIO 72 - Tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20. Ler um número pelo teclado e mostrar extenso.

print('=' * 20)
print('Número por Extenso')
print('=' * 20)

tupla = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um Número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente... ', end='')
print(f'Você digitou o Número: {tupla[num]}')
