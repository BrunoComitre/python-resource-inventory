# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 19:12:23 2018

@author: bruno
"""

# AULA EXTRA - Cores em Python

# STYLE - Existe de 0 a 7, mas esses funcionam melhor no Terminal.
# 0 - None - Vazio
# 1 - Bold - Negrito
# 4 - Underline - Sublinhado
# 7 - Negativo - Invertido

#TEXT - Cor do Texto
#30 Branco, 31 Vermelho, 32 Verde, 33 Amarelo, 34 Azul,
#35 Roxo, 36 Ciano, 37 Cinza

#BACK - Cor do Plano de Fundo
#40 Branco, 41 Vermelho, 42 Verde, 43 Amarelo, 44 Azul,
#45 Roxo, 46 Ciano, 47 Cinza

#Exemplo: \033[0;33;44m

nome = str(input('Digite o seu nome: '))

cores = {'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}

print('\033[0;30;41mTeste 1\033[m') #\033[m para não ultrapassar o texto digitado
print('\033[4;33;44mTeste 2\033[m e o \033[1;35;43mTeste 3')
print('\033[30;42mTeste 4') #Não declarado o style pois é o padrão. Poderia se 0
print('\033[mTeste 5') #Fica no padrão do Terminal
print('\033[7;30mTeste 6\033[m ') #7 Negativo do 33 Branco deixa a letra preta e o fundo branco

print('Olá Muito prazer em te conhecer, {}{}{}!!'.format(cores['azul'], nome, cores['limpa']))

