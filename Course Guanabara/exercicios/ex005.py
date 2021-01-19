# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:08:24 2018

@author: bruno
"""

#EXERCICIO 05 - Leia um número inteiro e mostre na tela seu sucessor e se antecessor.

'''n = int(input('Digite um Número:'))
ante = n - 1
suce = n + 1

print('O número digitado é: {},\nO seu Sucessor é: {},\nE seu antecessor é: {}.'.format(n, ante, suce))'''

# Outro jeito de se fazer

'''n = int(input('Digite um Número:'))
print('='*20)

ante = n - 1
suce = n + 1

print('O número digitado é: {:<20},\n'# Com 20 Caracteres alinhado a Esquerda
      'O seu Sucessor é: {:>20},\n'# Com 20 Caracteres alinhado a Direita
      'E seu antecessor é: {:^20}.'.format(n, ante, suce))# Com 20 Caracteres centralizado
print('Fim do Programa{:=^20}'.format(n))# Com 20 Caracteres centralizado, colocando iguais em volta'''

#Outro jeito com uma variável

'''n = int(input('Digite um Número:'))

print('O número digitado é: {},\n'
      'O seu Sucessor é: {},\n'
      'E seu antecessor é: {}.'.format(n, (n-1), (n+1)))'''

#Usando tudo na mesma Linha

n = int(input('Digite um Número:'))

print('O número digitado é: {}'.format(n), end=" ")# continua o print na mesma linha
print('O seu Sucessor é: {}'.format(n+1), end=" ")# continua o print na mesma linha
print('E seu antecessor é: {}'.format(n-1), end=" ")# continua o print na mesma linha
