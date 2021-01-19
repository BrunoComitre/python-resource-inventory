# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:44:52 2018

@author: bruno
"""

#EXERCÍCIO 71 - Simule um Caixa Eletrônico. Pergunte o Valor Sacado (Número Inteiro). E as Cédulas Entregues. Valor R$50 R$20 R$10 R$1.

print('=' * 30)
print('Simulador de Caixa Eletrônico')
print('=' * 30)

valor = int(input('Que valor Você quer Sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} Cédula(s) de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 35)
print('Volte Sempre! Tenha um Bom Dia!')
