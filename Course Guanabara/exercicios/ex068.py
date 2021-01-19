# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:00 2018

@author: bruno
"""

#EXERCÍCIO 68 - Jogue Par ou Ímpar, e o programa será interrompido quando o jogador perder. Mostre o total de Vitórias.

from random import randint

print('=' * 25)
print('Jogo do Par ou Ímpar')
print('=' * 25)

cont = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Diga um Valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()
    total = jogador + computador

    if total % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR')
        print('-' * 60)
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU ÍMPAR')
        print('-' * 60)
    if escolha in 'pP' and total % 2 == 0 or escolha in 'iI' and total % 2 == 1:
        print('VOCÊ GANHOU!')
        print('-' * 60)
        print('Vamos Jogar Novamente...')
    elif escolha not in 'pP' and total % 2 == 0 or escolha not in 'iI' and total % 2 == 1:
        print('VOCÊ PERDEU!')
        print('-' * 60)
        break
    cont += 1
print(f'GAME OVER!! Você Venceu {cont} vez(es)')
