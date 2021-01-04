string = 'Minha vó tem muitas jóias, só usa no prescoço'


x = string.split(' ')
y = string.split(',')
print(x)
print(y)

for valor in x:
    print(f'a palavra {valor}, apareceu {x.count(valor)} x na frase')

for valor in y:
    print(valor.strip()) # strip remove espaço em branco do início e do fim

juntar = ' '.join(x)
print(juntar)

for indice, valor in enumerate(x):
    print(indice, valor)
