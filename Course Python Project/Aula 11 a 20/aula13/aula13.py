# Esta aula é sobre formatação de valores

"""
Formatando valores com modificadores - Aula 13

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. - (NÚMERO)f - Quantidade de casas decimais (float)
:  - (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao:.2f}')

print('----' * 10)

nome = 'Bruno Alves Comitre'
print(f'{nome:s}')

print(f'{num_2:0>10}')  # Formatação preenchendo com zeros a esquerda com 10 casas somando o número

print(f'{num_1:.2f}')  # Tranformando em float

print(f'{num_1:0>10.2f}')  # Juntando as formatações

print(f'{nome:#^50}')  # Funciona com strings também - Deixando o nome no meio

nome_formatado = '{:@>50}'.format(nome)

print(nome_formatado)

print(nome.lower())  # Tudo Minúsculo
print(nome.upper())  # Tudo Maiúsculo
print(nome.title())  # Primeiras Letras Maiúsculas
