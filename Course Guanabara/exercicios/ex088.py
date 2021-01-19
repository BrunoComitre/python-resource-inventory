# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:37:49 2018

@author: bruno
"""

#EXERCÍCIO 88 - Crie palpites e pergunte quantos jogos serão gerados com 6 números entre 1 e 60. retorne para cada jogo lista composta.

print('-' * 30)
print('Palpites Para a Mega Sena')
print('-' * 30)

from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-' * 3, f' SORTEANDO {quant} JOGOS ', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('=-' * 5, '< BOA SORTE! > ', '=-' * 5)
