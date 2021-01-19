# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:26:32 2018

@author: bruno
"""

#EXERCÍCIO 14 - Converta a Temperatura de Celsius para Fahrenheit e Kelvin

c = float(input('Informe a Temperatura em ºC: '))

print('A Temperatura de {:.1f}ºC, corresponde a {:.1f}ºF, e {:.1f}ºK.'.format(c, ((9*c)/5)+32, c + 273,))
