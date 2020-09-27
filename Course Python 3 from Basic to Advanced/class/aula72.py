############ GROUPBY ############

from itertools import groupby, tee


alunos = [
    {'nome': 'Bruno', 'nota': 'A'},
    {'nome': 'Bruno', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Bruno', 'nota': 'B'},
    {'nome': 'João', 'nota': 'C'}
]

ordena = lambda item: item['nota']

alunos.sort(key=ordena)
# for aluno in alunos:
#     print(aluno)

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    
    for aluno in va1:
        print(aluno)
    
    print(agrupamento)
    quantidade = len(list(va2))
    print(quantidade)

############ MAP ############

produtos =  [
    {'nome': 'p1', 'preco': 12},
    {'nome': 'p2', 'preco': 45},
    {'nome': 'p3', 'preco': 87},
    {'nome': 'p4', 'preco': 4},
    {'nome': 'p5', 'preco': 54.14}
 ]

pessoas = [
    {'nome': 'Bruno', 'idade': 41},
    {'nome': 'Maria', 'idade': 25},
    {'nome': 'Ana', 'idade': 78},
    {'nome': 'Bruno', 'idade': 35},
    {'nome': 'João', 'idade': 15}
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista = map(lambda x: x*2, lista)
print(nova_lista)
print(list(nova_lista))

nova_lista = [x*2 for x in lista]
print(nova_lista)
print(list(nova_lista))

# precos = map(lambda p: p:['preço'], produtos)

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p
    
novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)
    
def aumenta_idade(p):
    p['nova_idade'] = p['idade'] * 1.20
    return p
    
nomes = map(aumenta_idade, produtos)
for pessoa in nomes:
    print(pessoa)

############ FILTER ############

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

# nova_lista = [x for x in lista if x > 5]  # usando list comprehension
# print(nova_lista)

produtos_filtrados = filter(lambda p: p['preco'] > 10, produtos)

for produto in produtos_filtrados:
    print(produto)

def filtro(p):
    if p['preco'] > 10:
        return True
    else:
        return False
    
produtos_filtrados = filter(filtro, produtos)
print(produtos_filtrados)

def filtro(produto):
    if produto['preco'] > 10:
        produto['e_caro'] = True
        return True
    
produtos_filtrados = filter(filtro, produtos)
print(produtos_filtrados)

def idade(p):
    if p['idade'] >= 18:
        return True
    else:
        return False
    
pessoas_filtradas = filter(idade, pessoas)
print(pessoas_filtradas)

for pessoa in pessoas_filtradas:
    print(pessoa)

############ REDUCE ############

from functools import reduce

soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda acumulador, produto: produto['preco'] + acumulador, produtos, 0)
print(soma_precos)
print(soma_precos / len(produtos))

soma_idade = reduce(lambda acumulador, pessoas: pessoas['idade'] + acumulador, pessoas, 0)
print(soma_idade)
print(soma_idade / len(pessoas))
