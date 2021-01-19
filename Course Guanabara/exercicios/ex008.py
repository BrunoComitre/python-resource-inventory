# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:12:00 2018

@author: bruno
"""

#EXERCÍCIO 08 - Leia um valor em metros e o exiba convertido em centimetros e milimetros.

d = float(input('Digite uma Distância em Metros: '))

print('A medida de {} corresponde a: \n'
      'Quilómetros (Km): {}\n'
      'Hectómetros (Hm): {}\n'
      'Decâmetros (Dam): {}\n'
      'Decímetros (Dm): {:.0f}\n'
      'Centímetros (Cm): {:.0f}\n'
      'Milímetros (Mm): {:.0f}'
      ''.format(d, (d/1000), (d/100), (d/10), (d*10), (d*100), (d*1000)))
