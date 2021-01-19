# Esta aula é sobre listas

"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# índice   0    1    2    3    4  
lista =  ['A', 'B', 'C', 'D', 'E', 10.5]
# neg -    -5   -4   -3   -2   -1

# Alterando o índice
lista[4] = 'Alteração'

# print(lista)
# print(lista[0:3])
# print(lista[:3])
# print(lista[::2])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

# Concatenando listas
l3 = l1 + l2

# print(l1)
# print(l2)
# print(l3)

l1.extend(l2)  # Concatena as duas listas
# print(l1)

l1.extend('a')  # Insere um  valor no final da lista
# print(l1)

# l2.append('b')  # Append insere um novo valor no final da lista
# print(l2)

l2.insert(0, 'banana')  # Insert insere qualquer valor em qualquer posição da lista
# print(l2)

l2.pop()  # Pop deleta a última posição da lista
# print(l2)

# Deletando elementos
new_list = [1, 2 ,3 ,4 ,5 ,6 ,7 ,8 , 9]
# print(new_list)

# del(new_list[3:5])
# print(new_list)

# Exibindo valores máximo e mínimo em uma lista
# print(f'Valor Máximo: ',max(new_list))
# print(f'Valor Mínimo: ',min(new_list))

# Criando uma Lista com Range
lista_range = list(range(1, 10))
# print(lista_range)

# lista_range = list(range(1, 100,8))
# print(lista_range)

# soma = 0
# for valor in lista_range:
#     soma += valor
# print(soma)

lista_diversa = ['String', True, 10, -20.5]

# for elem in lista_diversa:
#     print(f'O seu valor é {elem}, e o tipo de elem é {type(elem)}')

# JOGO DE ADIVINHAÇÃO DE PALAVRA SECRETA

secret = 'python'
letras_digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('Você perdeu')
        break

    letra = str(input('Digite uma letra: '))

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra')
        continue

    letras_digitadas.append(letra)

    if letra in secret:
        print(f'Uhull, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'Afffzz, a letra "{letra}" não existe na palavra secreta')
        letras_digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secret:
        if letra_secreta in letras_digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secret:
        print(f'Que legal você ganhou. A palavra era: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secret:
        chance -= 1

    print(f'Você ainda tem {chance} chances')
    print()
