# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:01 2018

@author: bruno
"""

#EXERCÍCIO 62 - Melhore o Exercício 61, perguntado para o usuário se ele quer mostrar mais alguns termos. Encerrar quando mostrar 0 Termos.

print('=' * 35)
print('Progressão Aritmética Melhorado')
print('=' * 35)

num = int(input('Primeiro Termo: '))
razao = int(input('Razão da Progressão Aritmética: '))
pa = num + (10 - 1) * razao
cont = num
termo = 0
while cont != pa + razao:
    print('{} → '.format(cont), end='')
    cont += razao
    termo += 1
    if cont == pa + razao:
        print('PAUSA')
        termos = int(input('Quantos Termos você quer mostrar a mais? '))
        pa = pa + termos * razao
print('Progressão finalizada com {} Termos mostrados.'.format(termo))
