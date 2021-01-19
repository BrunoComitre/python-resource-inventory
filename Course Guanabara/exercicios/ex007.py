# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:12:01 2018

@author: bruno
"""

#EXERCÍCIO 07 - Leia as duas notas de um aluno e calcule e mostre a sua média.

n1 = float(input('Digite a Primeira Nota:'))
n2 = float(input('Digite a Segunda Nota: '))

print ('A Média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2 ,((n1+n2)/2)))
