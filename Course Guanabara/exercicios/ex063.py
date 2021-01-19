# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:01 2018

@author: bruno
"""

#EXERCÍCIO 63 - Leia um número inteiro e mostre os n primeiros elementos de uma Sequência de Fibonacci.

print('=' * 25)
print('Sequência de Fibonacci')
print('=' * 25)

num = int(input('Quantos Termos você quer mostrar? '))
t1 = 0
t2 = 1

print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
