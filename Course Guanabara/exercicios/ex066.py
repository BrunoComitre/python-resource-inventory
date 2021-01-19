# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:00 2018

@author: bruno
"""

#EXERCÍCIO 66 - Leia Números Inteiros, pare ao digitar 999, mostre os números digitados e a soma sem somar a FLAG.

print('=' * 20)
print('Cálculo dos Números')
print('=' * 20)

soma = cont = 0
while True:
    try:
        num = int(input('Digite um Número Inteiro [999 para parar]: '))
    except:
        print('Erro. Valor incorreto!')
        continue
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A Soma do(s) {cont} Valore(s) foi {soma}!')
