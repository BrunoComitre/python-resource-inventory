# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:00 2018

@author: bruno
"""

#EXERCÍCIO 69 - Leia Idade e Sexo das pessoas. Mostre mais de 18 Anos. Quantos Homens. Quantas Mulheres com menos de 20 Anos.

print('=' * 30)
print('Análises de Dados do Grupo')
print('=' * 30)

mulhermenosdevinte= m = m18 = 0
while True:
    print('-'*50)
    print(f'{"CADASTRE UMA PESSOA":^50}')
    print('-'*50)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        m += 1
    if idade > 18:
        m18 += 1
    if sexo == 'F':
        if idade < 20:
            mulhermenosdevinte += 1
    escolha = str(input('Deseja Continuar [S/N]? ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja Continuar? [S/N]? ')).upper().strip()
    if escolha == 'N':
        break
print('==========FIM DO PROGRAMA==========')
print(f'Total de Pessoa(s) com mais de 18 Anos: {m18}.')
print(f'Ao todo temos {m} Homens Cadastrados.')
print(f'E temos {mulhermenosdevinte} Mulhere(s) com menos de 20 Anos.')
