# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:05 2018

@author: bruno
"""

#EXERCÍCIO 43 - Receba Peso e Altura, e calcule o IMC da Pessoa.

print('=' * 20)
print('Cállculo de IMC')
print('=' * 20)

peso = float(input('Qual é o seu Peso (Kg)? '))
altura = float(input('Qual é a sua Altura (m)? '))

imc = peso/(altura ** 2)

if imc <= 18.5:
    print('Seu IMC é de {:.2f}. Você está ABAIXO DO PESO.'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f}. Você está no PESO IDEAL.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f}. Você está com SOBREPESO.'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.2f}. Você está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))
    