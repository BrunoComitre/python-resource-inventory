# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:05 2018

@author: bruno
"""

#EXERCÍCIO 41 - Receba a data de Nascimento, e mostre a categoria de acordo com a idade.

from datetime import date

print('=' * 30)
print('Classificação Esportiva')
print('=' * 30)
        
atual = date.today().year #Colocar o ano atual
ano = int(input('Qual é o seu Ano de Nascimento? '))

if (ano > 0) and (atual > ano): #Verificar se nao vai digitar um numero negativo ou ano atual é maior o ano
    idade = atual - ano
    
    se ano maior que 0 e atual maior que ano
    idade recebe ano atual 2019 menos anos de nascimento
    
    
    if idade <= 9:
        print('A idade é {} anos e um atleta para categoria Mirin'.format(idade))
    elif 14 >= idade > 9:
        print('A idade {} anos e um atleta para categoria Infantil'.format(idade))
    elif 19 >= idade > 14:
        print('A idade {} anos e um atleta para categoia Junior'.format(idade))
    elif 25 >= idade > 19:
        print('A idade {} anos e um atleta para categoria Senior'.format(idade))
    elif idade > 25:
        print('A idade {} anos e um atleta para categoia Master'.format(idade))

elif ano < 0: #Verificar se um número negativo
    print('Você digitou um número negativo! Digite novamente')
elif ano > atual: #Se o ano é maior ano atual
    print('Você Ainda Não Nasceu!')
else: #Verificar o Ano Atual 
    print('Criança acabou de nascer!')
    