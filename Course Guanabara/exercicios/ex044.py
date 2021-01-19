# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:04 2018

@author: bruno
"""

#EXERCÍCIO 44 - Calcule o Valor a ser Pago de um Produto considerando o tipo do Pagamento.

print('=' * 20)
print('Formas de Pagamentos')
print('=' * 20)

compra = float(input('Preço das Compras: R$ '))

print('''FORMAS DE PAGAMENTO 
      [ 1 ] - À Vista Dinheiro/Cheque 
      [ 2 ] - À Vista no Cartão 
      [ 3 ] - 2x no Cartão 
      [ 4 ] - 3x ou mais no Cartão''')

escolha = int(input('Qual é a Opção: '))

if escolha == 1:
    valor = compra - (compra * 10 / 100)
    print('O valor é de {:.2f}, mas como vai ser pago a vista em "Dinheiro" ou "Cheque", tem 10% de Desconto.\n'
          'O valor será de R${:.2f}'.format(compra, valor))

elif escolha == 2:
    valor = compra - (compra * 5 /100)
    print('O valor é de R${:.2f}, mas como vai ser pago à vista no "Cartão", com 5% de Desconto \n'
          'O valor será de R${:.2f}'.format(compra, valor))

elif escolha == 3:
    valor = compra / 2
    print('O valor é de R${:.2f}. Pagando em 2X no "Cartão", pagando valor Normal\n'
          'O valor será de R${:.2f} cada parcela'.format(compra, valor))

elif escolha == 4:
    parc = int(input('Digite a Quantidade de Parcelas: '))
    nvalor = compra + (compra * 20 / 100)
    valor = nvalor / parc
    print('O valor é de R${}, para pagar em {}X será de R${:.2f} de cada parcela'
          '\nO valor total a pagar é R${:.2f} em {}X com o acréscimo de 20% de Juros'.format(compra, parc, valor, nvalor, parc))

else:
    print('Valor Digitado Incorreto')
    
print('OBRIGADO E VOLTE SEMPRE!!')

            