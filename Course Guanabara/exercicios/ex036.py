# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:02 2018

@author: bruno
"""

#EXERCÍCIO 36 - Empréstimo Compra Casa - Recebe valor, casa, anos, não exceder 30%.

print('=' * 35)
print('Programa Meu Python, Minha vida')
print('=' * 35)

casa = float(input('Qual o valor da Casa: R$ '))
salario = float(input('Quanto é o seu Salário R$: '))
anos = int(input('Quantos anos de Financiamento? '))

meses = anos*12
parcela = casa/meses
porcentagem = salario*30/100

if parcela >= porcentagem:
    print('Desculpe, Empréstimo foi NEGADO, pois, o valor da parcela mensal de {:.2f} excedeu 30% do seu salário.'.format(parcela))
else:
    print('Parabéns, Empréstimo foi AUTORIZADO. Comprando esta casa em {} ano(s), a parcela mensal será de {:.2f}.'.format(anos, parcela))    