# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 39 - Receba ano. Mostre o alistamento e quanto tempo falta.

from datetime import date

print('=' * 30)
print('Alistamento Militar')
print('=' * 30)

ano = int(input('Em que Ano você Nasceu? '))
print('''Informe o seu sexo:
[ 1 ] Masculino
[ 2 ] Feminino''')
sexo = int(input('Você é do Sexo: '))

idade = date.today().year - ano

if sexo == 2:
    print('Você não é obrigada ao alistamento.')
    sim_nao = str(input('Você Gostaria de se alistar nas Forças Armadas? Sim ou Não? ')).title().strip()
    
    if sim_nao == 'Não':
        print('Tenha um bom dia Senhorita!')
    elif sim_nao == 'Sim':
        print('BEM-VINDA Ao Serviço Militar!')
        
        if idade == 18: 
            print('Você tem que se alistar IMEDIATAMENTE!') 
        elif idade > 18:
            alistamento = idade - 18
            ano = date.today().year - alistamento 
            print('Você já deveria ter se alistado há {} ano(s)'.format(alistamento))
            print('Seu alistamento foi em {}'.format(ano))
        else:
            alistamento = 18 - idade
            ano = alistamento + date.today().year
            print('Ainda faltam {} ano(s) para o alistamento'.format(alistamento))
            print('Seu alistamento será em {}'.format(ano))   
    else:
        print('Entrada inválida, escolhar Sim ou Não')
        
elif sexo == 1:
    print('BEM-VINDO ao Serviço Militar')
    if idade == 18:
        alistamento = 18  
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        alistamento = idade - 18
        ano = date.today().year - alistamento 
        print('Você já deveria ter se alistado há {} ano(s)'.format(alistamento))
        print('Seu alistamento foi em {}'.format(ano))
    else:
        alistamento = 18 - idade
        ano = alistamento + date.today().year
        print('Ainda faltam {} ano(s) para o alistamento'.format(alistamento))
        print('Seu alistamento será em {}'.format(ano))
        
else:
    print('Entrada Inválida!')
