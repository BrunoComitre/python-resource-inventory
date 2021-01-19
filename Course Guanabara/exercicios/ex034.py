# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:36:38 2018

@author: bruno
"""

#EXERCÍCIO 34 - Receba o salário do funcionário e calcule o aumento.
# Superior a R$ 1.250,00 aumento de 10%. Para inferiores ou iguais, aumento de 15%.

salario = float(input('Qual é o Salário do Funcionário? R$ '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario, novo))
