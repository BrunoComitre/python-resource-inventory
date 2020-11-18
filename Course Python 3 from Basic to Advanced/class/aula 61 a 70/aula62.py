lista  = [
    ('chave1', 2),
    ('chave2', 'valor2')
]

d1 = {x: y  for x, y in lista}
print(d1)

d2 = {x.upper(): y*2  for x, y in lista}
print(d2)
 
d3 = {x: y for x, y in enumerate(range(5))}
print(d3)

d4 = {x for x in range(5)}
print(d4, type(d4))

d5 = {f'chave_{x}': x**2 for x in range(5)}
print(d5)
