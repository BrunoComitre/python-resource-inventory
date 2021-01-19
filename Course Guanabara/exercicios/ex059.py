# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:01 2018

@author: bruno
"""

#EXERCÍCIO 59 - Receba 2 valores. Crie um programa que soma, multiplique, maior,novos números, sair do programa.

from time import sleep

print('=' * 25)
print('Calculadora em Python')
print('=' * 25)

num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))

menu = 0
while menu != 5:
  menu = int(input('''ESCOLHA UMA OPÇÃO NO MENU:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] sair Do programa
    '''))
  if menu == 1:
    print('A Soma Entre {} e {} é de {}'.format(num1, num2, num1 + num2))
    sleep(1)
  elif menu == 2:
    print('O Número {} Multiplicado por {} é {}'.format(num1, num2, num1 * num2))
    sleep(1)
  elif menu == 3:
    if num1 > num2:
      print('O Número {} é Maior'.format(num1))
    else:
      print('O Número {} é Maior'.format(num2))
    sleep(1)
  elif menu == 4:
      print('Informe os Números Novamente:')
      num1 = int(input('Digite o Primeiro Número: '))
      num2 = int(input('Digite o Segundo Número: '))
  elif menu == 5:
      print('Programa Finalizado.')
  else:
      print('Opção Invalida. Tente Novamente.')
