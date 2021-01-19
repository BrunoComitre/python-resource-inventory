# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:40 2018

@author: bruno
"""

#EXERCÍCIO 75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

print('=' * 30)
print('Análise de Dados em uma Tupla')
print('=' * 30)

num = (int(input('Digite o Primeiro Número: ')),
      int(input('Digite o Segundo Número: ')),
      int(input('Digite o Terceiro Número: ')),
      int(input('Digite o Quarto Número: ')))

print(f'Você Digitou os Valores: {num}')
print(f'O Valor 9 Apareceu {num.count(9)} Veze(s)')
if 3 in num:
    print(f'O Valor 3 Apareceu na {num.index(3)+1}º Posição')
else:
    print('O valor 3 Não Foi Digitado em Nenhuma Posição')    
print('Os Valores Pares Digitados Foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
        