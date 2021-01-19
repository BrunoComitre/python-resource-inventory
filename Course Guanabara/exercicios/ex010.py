# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:11:58 2018

@author: bruno
"""

#EXERCÍCIO 10 - Leia quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$ 1,00 = R$ 3,27

real = float(input('Quanto dinheiro você tem na Carteira? R$:'))

print ('=' *12)
print ('Com Real:{:.2f} R$ você pode comprar:\n'
       'Dólar: {:.2f} US$,\n'
       'Dinar:{:.2f} IQD$,\n'
       'Iene:{:.2f} ¥$,\n'
       'Rublo:{:.2f} P$,\n'
       'Peso:{:.2f} ARS$.'
       ''.format(real, (real/3.31), (real/10.908), (real/0.029), (real/0.056), (real/0.196)))
print ('=' *12)
