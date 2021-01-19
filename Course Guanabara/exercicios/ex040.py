# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:45:03 2018

@author: bruno
"""

#EXERCÍCIO 40 - Receba duas notas. Exiba Reprovado, Recuperação, Aprovado.

print('=' * 20)
print('Nota Escolar')
print('=' * 20)

nome = str(input('Informe seu nome: ')).strip()
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if 7.0 <= media <= 10:
 print('Aluno: {}\nPrimeiro Bimestre: {:.1f}\nSegundo Bimestre: {:.1f}\nMédia: {:.1f}\nO Aluno {} foi '
       'APROVADO!'.format(nome, nota1,nota2, media, nome))
elif 5 <= media < 6.9:
 print('Aluno: {}\nPrimeiro Bimestre: {:.1f}\nSegundo Bimestre: {:.1f}\nMédia: {:.1f}\nO Aluno {} está de '
       'RECUPERAÇÃO.'.format(nome, nota1, nota2, media, nome))
elif 0 <= media < 5:
 print('Aluno: {}\nPrimeiro Bimestre: {:.1f}\nSegundo Bimestre: {:.1f}\nMédia: {:.1f}\nO Aluno {} está '
       'REPROVADO.'.format(nome, nota1, nota2, media, nome))
else:
    print('As notas vão de 0 a 10, Por Favor, Insira Novamente.')
    