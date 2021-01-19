# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:12:47 2018

@author: bruno
"""

#EXERCÍCIO 24 - Leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

c = str(input('Em qual cidade você Nasceu? ')).strip()#O strip elimina os espaços do texto
print('Essa cidade começa com a palavra Santo: {}'.format(c[:5].upper() =='SANTO'))
