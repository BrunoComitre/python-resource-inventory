# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:01:08 2018

@author: bruno
"""

#EXERCÍCIO 28 - Computador pensa num número de 0 a 5. E tente descobrir.
# Programa escreve na tela se usuário ganhou ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador gerar um número aleatório

print('-=-' * 20)
print('Vou pensar em um Número entre 0 e 5. Tente Advinhar...')
print('-=-' * 20)

jogador = int(input('Em que Número eu pensei? '))

print('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print('PARABÉNS! Você consegui me vencer!!!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
