# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:36:35 2018

@author: bruno
"""

#EXERCÍCIO 29 - Leia a velocidade de um carro. Se passar de 80Km/h, escreva multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

v = float(input('Qual a Velocidade atual do Carro? '))

if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (v - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f} '.format(multa))
print('Tenha um bom dia! Dirija com Segurança!')
