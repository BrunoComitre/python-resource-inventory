"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação -  Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos    
"""

from itertools import combinations, permutations, product

pessoa = ['Bruno', 'João', 'Maria', 'Ana', 'José', 'Vilma']

for grupo in combinations(pessoa, 3):
    print(grupo)

for grupo in permutations(pessoa, 2):
    print(pessoa)
    
for grupo in product(pessoa, repeat=2):
    print(pessoa)