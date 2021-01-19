# Esta aula é sobre operadores relacionais

"""
Operadores Relacionais - Aula 11
==  igualdade
>   maior
>=  maior que ou igual a
<   menor
<=  menor que ou  igual a
!=  diferente de
"""

# Funciona tanto para NÚMEROS quanto para STRINGS

num_1 = 2  # int
num_2 = 2  # int

igual_a = (num_1 == num_2)  # ==
maior_que = (num_1 > num_2)  # >
maior_que_ou_igual_a = (num_1 >= num_2)  # >= 
menor_que = (num_1 < num_2)  # <
menor_que_ou_igual_a = (num_1 <= num_2)  # <= 
diferente_de = (num_1 != num_2)  # !=

print(igual_a)
print(maior_que)
print(maior_que_ou_igual_a)
print(menor_que)
print(menor_que_ou_igual_a)
print(diferente_de)

nome = input('Qual o seu nome ? ')
idade = int(input('Qual a sua idade ? '))

#Limite para pegar empréstimo

idade_jovem = 20
idade_velho = 30

if idade >= idade_jovem and idade <= idade_velho:
    print(f'{nome}, pode pegar o empréstimo')
else:
    print(f'{nome}, não pode pegar o empréstimo') 
