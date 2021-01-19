# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:04 2018

@author: bruno
"""

#EXERCÍCIO 45 - Crie um Programa que faça o Computador jogar Jokenpô com Você.

from random import choice
from time import sleep

print('=' * 15)
print('Jogo Jokenpô')
print('=' * 15)

nome = str(input('Seu Nome de Jogador: ')).strip()
computador = ['pedra', 'papel', 'tesoura']
time = 0

while time == 0:
    print('''Suas Opções:
        * Pedra
        * Papel
        * Tesoura''')
    jogador = str(input('Qual é a Sua Jogada? ')).lower()
    if jogador == 'pedra' or jogador == 'papel' or jogador == 'tesoura':
        time = 1
        jogo = choice(computador)
        
print("1")
sleep(1)
print("2")
sleep(1)
print("3, e já!!")
sleep(0.4)

if jogo == jogador:
    print('{} escolheu {} e o COMPUTADOR escolheu {}, temos um empate!!'.format(nome, jogador, jogo))
elif jogo == 'pedra' and jogador == 'tesoura' or jogo == 'papel' and jogador =='pedra' or jogo == 'tesoura' and jogador == 'papel':
    print('{} escolheu {} e o COMPUTADOR escolheu {}, COMPUTADOR venceu!!!'.format(nome, jogador, jogo))
else:
    print('{} escolheu {} e o COMPUTADOR escolheu {}, {} venceu!!!'.format(nome, jogador, jogo, nome))
