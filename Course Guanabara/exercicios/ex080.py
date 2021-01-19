# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:42 2018

@author: bruno
"""

#EXERCÍCIO 80 - O usuário digita 5 valores e cadastre na lista, já na posição correta de inserção (sem usar sort()), mostre lista ordenada.

print('=' * 30)
print('Lista Ordenada sem Repetições')
print('=' * 30)

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor da posição: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos+1} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {lista}')
