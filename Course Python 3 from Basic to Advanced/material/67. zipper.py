"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
