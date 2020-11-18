"""
append, insert, pop, del, clear, extend, +, min, max, range
"""

texto_string = 'valor'
lista_exemplo = [1, 2, 3, 4, 'Python', True, 10.0]

lista = ['Python', 'Aula', 'Teste']

for valor in lista:
    if valor.startswith('A'):
        print('Começa com A')
        break
else:
    print('Não começa com A')