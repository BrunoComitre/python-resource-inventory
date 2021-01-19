# Esta aula é sobre Split, Join e Enumerate

"""
Split, Join e Enumerate
* Split     - Dividir uma string          # str 
* Join      - Juntar uma lista            # str
* Enumerate - Enumerar elementos da lista # list
"""

"""
# SPLIT
string = 'O Brasil é o país do Futebol, O Brasil é penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

# print(lista_1)
# print(lista_2)

# for valor in lista_1:
#     print(f'A palavra {valor}, apareceu {lista_1.count(valor)} vezes na frase')

palavra = ''
contagem = 0

for valor in lista_1:
    quantidade_de_vezes = lista_1.count(valor)

    if quantidade_de_vezes > contagem:
        contagem = quantidade_de_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}) vezes')

for valor in lista_2:
    print(valor.strip().capitalize())

# OBSERVAÇÃO - Isso se parece muito com a Aula de MapReduce, que o Matheus fez exemplos na sala em 20/07/2019
"""

"""
# JOIN
string = 'O Brasil é Penta'
lista = string.split(' ')

string_2 = ','.join(lista)

print(string)
print(lista)
print(string_2)
"""

# ENUMERATE
"""
string = 'O Brasil é Penta'
lista = string.split(' ')

for indice, valor_real in enumerate(lista):  # indice, valor_real significa que você está desempacotando o elemento que como no exemplo é o enumerate
    print(indice, valor_real, lista[indice])
"""


lista = [
    [1, 'Bruno'],
    [3, 'João'],
    [5, 'Maria']
]

# for valor in lista:
#     print(valor[0], valor[1])

# OBSERVAÇÃO -  A função enumerate retorna Tuplas

for indice, valor in lista:
    print(indice, valor)

for indice, valor_real in enumerate(lista):
    print(indice, valor_real)

"""
lista = ['Bruno', 'João', 'Maria']

n1, n2, n3 = lista

print(n2)
"""
