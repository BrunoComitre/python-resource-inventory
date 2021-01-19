# Esta aula é sobre desempacotar listas

"""
Desempacotando listas
"""

lista = ['Bruno', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

# n1, n2, n3 = lista
# print(n1,n2, n3)

# n1, n2, n3, *outra_lista = lista
# print(n1,n2, n3)
# print(outra_lista)

# n1, n2, n3, *outra_lista = lista
# print(n1,n2, n3)
# print(outra_lista)
# print(outra_lista)  # Pegando o último valor

# n1, n2, n3, *outra_lista, ultimo_valor = lista
# print(n1,n2, n3)
# print(outra_lista)
# print(ultimo_valor)  # Pegando o último valor

# *outra_lista, n1, n2, n3 = lista
# print(n1,n2, n3)
# print(outra_lista)

n1, n2, *_ = lista  # _ (underline) como variável significa que você nâo vai utilizada no restante do código
print(n1,n2)
print(_)
