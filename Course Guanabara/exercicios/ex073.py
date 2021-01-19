# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:33:38 2018

@author: bruno
"""

#EXERCÍCIO 73 -  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre: A) Os 5 primeiros. B) Os últimos 4 colocados. C) Times em ordem alfabética. D) Em que posição está o time da Chapecoense.

print('=' * 30)
print('Tuplas com Times de Futebol')
print('=' * 30)

tupla = ('São Paulo', 'Flamengo', 'Grêmio', 'Internacional', 'Atlético-MG', 
         'Palmeiras', 'Corinthians','Cruzeiro', 'Fluminense', 'Botafogo',
         'América-MG', 'Bahia', 'Chapecoense', 'Sport', 'Vasco', 'Vitória',
         'Santos', 'Ceará', 'Atlético-PR', 'Paraná')
print('-=' * 70)
print(f'Lista de Times do Brasileiro: {tupla}')
print('-=' * 70)
print(f'Os 5 Primeiros São: {tupla[0:5]}')
print('-=' * 45)
print(f'Os 4 últimos São: {tupla[-4:]}')
print('-=' * 70)
print(f'Os Times em Ordem Alfabética: {sorted(tupla)}')
print('-=' * 70)
print(f'A Chapecoense está na Posição: {tupla.index("Chapecoense")+1}ª')
print('-=' * 20)
