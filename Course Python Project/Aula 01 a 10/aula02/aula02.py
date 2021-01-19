# Esta é uma aula sobre print

#  print(123456)

"""
print('Bruno', 'Alves', 'Comitre')

print('Bruno', 'Alves', 'Comitre', sep='-')
"""

print('Para', 'exibir', 'texto ', sep='-', end='')

print('sem', 'separar', 'por quebra de linha', 'se usa o end=''', sep='-', end='')

print()  # Assim também pode se usar para quebrar linha

print('Para', 'exibir', 'texto ', sep='-', end='######')

print('usando', 'end', 'diferente', 'se usa o end=''', sep='-', end='\n')  # Usando exemplo \n, para quebrar linha

print('Exercício:')

"""
Exiba o CPF: 824.176.070-18
"""

# Versão Bruno
print('824', '176.', sep='.', end='')
print('070', 18, sep='-', end='')

print()

# Versão Professor
print('824', '176','070', sep='.', end='-')
print(18)
