# Esta aula é sobre tipos de dados primitivos

"""
Tipos de dados:

str - string
textos 'Assim' "Assim"

int - inteiro
123456 0 -10 

float - real/ponto flutuante
-10.8 0.0 10.8

bool - booleano/lógico
True ou False
"""

print('----'*10)

print('Isto é uma string: ', 'Bruno :', type('Isto é uma string'))  # String

print('----'*10)

print('Isto é um inteiro: ', 123456, ':', type(123456))  # Inteiro

print('----'*10)

print('Isto é um float: ', 10.0, ':', type(10.0))  # Float

print('----'*10)

print('Isto é um booleano: ', 10 == 10, ':', type(True))  # Bool

print('----'*10)

# Exercicio:

# Nome: string
print('Bruno Alves Comitre', type('Bruno Alves Comitre'))

# Idade: int
print(25, type(23))

# Altura: float
print(1.83, type(1.83))

# Maior de Idade: bool
print(25 > 18, type(24 > 18))
