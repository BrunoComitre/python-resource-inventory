# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:44:53 2018

@author: bruno
"""

#EXERCÍCIO 70 - Leia Nome e Preço dos Produtos. Mostre total gasto, produtos que custam mais de R$ 1000 e o Produto mais barato. 

print('=' * 25)
print('Estatísticas em Produtos')
print('=' * 25)

total = produtos = barato = soma = count = 0
nome2 = ''

while True:
    nome = str(input('Nome do Produto: '))
    pr = float(input('Preço do Produto: R$ '))

    soma += pr
    count += 1

    pergunta = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if pergunta != 'S' and pergunta != 'N':
        while pergunta != 'S' and pergunta != 'N':
            print('Apenas S para SIM ou N para NÃO!!')
            pergunta = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]

    print('---' * 10)
    if pr > 1000:
        produtos += 1
    if count == 1 or pr < barato:
        barato = pr
        nome2 = nome
    if pergunta == 'N':
        print('==== FIM DO PROGRAMA ====')
        print(f'O Total da Compra foi R$ {soma}.')
        print(f'Temos {produtos} Produto(s) custando mais de R$ 1000.00.')
        print(f'O Produto mais barato foi {nome2} que custa R$ {barato}.')
        break
    