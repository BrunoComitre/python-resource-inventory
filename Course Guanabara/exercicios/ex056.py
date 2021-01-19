# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:02 2018

@author: bruno
"""

#EXERCÍCIO 56 - Leia Nome, Idade, Sexo. E Mostre, a média de idade do grupo, nome do mais velho, quantas mulheres têm menos de 20 anos.

print('=' * 20)
print('Idade das Pessoas')
print('=' * 20)

somaidade = 0
mediaidade = 0
maisvelho = 0
nomemaisvelho = ''
totmulher = 0

for c in range(1, 5):
    print(str('----{}ª PESSOA ----'.format(c)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo =='M' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    if sexo =='F' and idade < 20:
        totmulher += 1
        
mediaidade = somaidade / 4

print('A Média de idade do grupo é de: {} anos.'.format(mediaidade))
print('O Homem mais velho têm {} anos, e se chama {}.'.format(maisvelho, nomemaisvelho))
print('Ao todo são {} Mulher(es) com menos de 20 anos.'.format(totmulher))

# Outro Jeito de Se Fazer

'''import os

nomes = [] # Armazena os nomes das pessoas
idades = [] # Armazena as idades das pessoas
sexos = [] # Armazena os sexos das pessoas
soma = 0 # Soma as idades das pessoas
maisVelho = 0 # Armazena a idade do homem mais velho
nomeM = '' # Concatena nome e idade do homem mais velho
mSub20 = 0 # Armazena a quantidade de mulheres com idades abaixo de 20 anos
nomeF = '' # Concatena nome e idade das mulheres abaixo de 20 anos
for i in range(0, 4):
    print(str(i+1) + 'ª' + ' pessoa: ')
    nomes.append(input('Nome: ').capitalize())
    idades.append(int(input('Idade: ')))
    sexos.append(input('Sexo(M/F): ').upper())
    soma += idades[i]
    if sexos[i] == 'F' and idades[i] < 20:
        nomeF += nomes[i] + ',' + str(idades[i]) + ' anos; '
        mSub20 += 1

for i in range(0, len(idades)):
    if sexos[i] == 'M' and idades[i] > maisVelho:
        maisVelho = idades[i]
        nomeM = nomes[i]
print('Média de idade do grupo: {:.2f} anos.'.format(soma/4))
print('Homem mais velho: {}, {} anos.'.format(nomeM, maisVelho))
print('Mulheres acima de 20 anos: {}. {}'.format(mSub20, nomeF))'''
