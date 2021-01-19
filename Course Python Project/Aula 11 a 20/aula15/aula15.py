# Esta aula é sobre a estrutura de Repetição While

"""
while em Python

Utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

# while condicao:
#    pass

# while True:  # Loop Infinito
#    nome = input('Quao o seu nome ? ')
#    print(f'Olá {nome}!')

"""
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue  # A palavra continue pula para o próximo laço
    print(x)
    x += 1

print('End')
"""

"""
x = 0
while x < 10:
    if x == 3:
        x += 1
        break  # A palavra break finaliza o loop
    print(x)
    x += 1

print('End')
"""

"""
x = 0  # coluna
while x < 10:
    y = 0  # linha y:0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1
print('End')
"""

# Exemplo Calculadora

while True:
    print()
    num_1 = input('Numero 1: ')
    num_2 = input('Numero 2: ')
    operator = input('Digite um operador:')
    sair = input('Deseja sair ? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Digite apenas Números')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(f' A soma é {num_1 + num_2}')
    elif operator == '-':
        print(f' A subtração é {num_1 - num_2}')
    elif operator == '/':
        print(f' A divisão é {num_1 / num_2}')
    elif operator == '*':
        print(f' A multiplicação é {num_1 * num_2}')
    else:
        print('Operador Inválido')
        break

print('End')
