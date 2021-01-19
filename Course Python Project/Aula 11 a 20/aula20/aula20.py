# Esta aula é sobre for / else

"""
For / Else
"""

variavel = ['Bruno', 'João', 'Maria']

comeca_com_b = False

"""
for valor in variavel:
    if valor.lower().startswith('B'):
        comeca_com_b = True

if comeca_com_b:
    print('Existe uma palavra que começa com B')
else:
    print('Não existe palavra que começa com B')
"""

"""
for valor in variavel:
    print(valor)
    if valor.lower().startswith('b'):
        break

else:
    print('Não existe palavra que começa com B')
"""

for valor in variavel:
    if valor.lower().startswith('b'):
        #pass
        continue
    print(valor)

else:
    print('Não existe palavra que começa com B')
