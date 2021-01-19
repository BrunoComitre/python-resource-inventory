# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:01 2018

@author: bruno
"""

#EXERCÍCIO 58 - No Exercício 28. Pense num número entre 0 e 10. Adivinhe e mostra quanstas vezes foi necessário para acertar o palpite.

from random import randint

print('=' * 20)
print('Acerte o Número')
print('=' * 20)

computador = randint(0, 10)
print('♦  O Computador vai escolher um Número de 0 até 10. Tente Adivinhar  ♦')

jogador = int(input('Digite um Número entre 0 e 10: '))
soma = 0
while computador != jogador:
    jogador = int(input('Você Errou. Tente Novamente: '))
    soma += 1
    if computador == jogador:
        print('Parabéns! Você Ganhou. O Número do Computado foi {} e o seu foi {}.'.format(computador, jogador))
print('Você precisou de {} Tentetivas para Acertar o Número.'.format(soma))

# Outro Jeito de se Fazer

'''from random import randint
from time import sleep

print('♦   Vamos Jogar um jogo? Vou pensar num numero de 0 a 5   ♦')
sleep(3)
print('♦ Você tem 5 tentativas!  ♦ A cada erro você perde um ponto.  ♦ Se você chegar a 0 pontos você perde!')
sleep(5)
pontuacao = 10
nome = int(input('Escolha um número de 0 a 5 : '))
resposta = randint(0, 5)
tentativa = 1
print('PROCESSANDO..........')
sleep(2)
while not nome == resposta:
    tentativa += 1
    if nome > resposta:
        nome = int(input('Errou! Tente um número menor!: '))
        print('Processando...')
        sleep(1)
    elif nome < resposta:
        nome = int(input('Errou! Tente um número maior!: '))
        print('Processando...')
        sleep(1)
    pontuacao -= 2
    if tentativa > 5:
        print('GAME OVER! O computador escolheu o número {}'.format(resposta))
if pontuacao >= 0:
    print('Acertou! O computador escolheu o número {}. Você fez um total de {} pontos'.format(resposta, pontuacao))
else:
    print('GAME OVER! O computador escolheu o número {}'.format(resposta))'''
