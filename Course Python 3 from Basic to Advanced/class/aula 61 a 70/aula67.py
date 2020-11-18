"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Sorocaba']
estados = ['SP', 'MG', 'BA']

# cidades_estados = zip(
#     indice,
#     estados,
#     cidades
# )

# print(cidades_estados)
# print(list(cidades_estados))
# print(dict(zip(estados,cidades)))

cidades_estados = zip_longest(
    estados,
    cidades,
    fillvalue='Estado'
)
print(list(cidades_estados))


for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
