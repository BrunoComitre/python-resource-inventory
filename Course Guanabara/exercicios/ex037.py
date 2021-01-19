# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:04 2018

@author: bruno
"""

#EXERCÍCIO 37 - Leia número inteiro. E converta 1 Binário, 2 Octogonal, 3 Hexadecimal.
 
print('=' * 20)
print('Conversão de Base')
print('=' * 20)

num = int(input('Digite um Número Inteiro: '))

print('''Escolha uma das bases para Conversão: 
[ 1 ] converter para Binario
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')

converte = int(input(' Sua Opção: '))

if converte == 1:
    print('seu número {} foi convertido para Binario: {}'.format(num, bin(num)[2:]))
elif converte == 2:
    print('Seu número {} foi convertido para Octagonal: {}'.format(num, oct(num)[2:]))
elif converte == 3:
    print('Seu número {} foi convertido em Hexadecimal: {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida. Tente Novamente!')
