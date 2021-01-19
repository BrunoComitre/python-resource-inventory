# Esta aula é sobre estrutura de repetição For in

"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

text = 'Python'

# for letter in text:
#     print(letter)

# for number in range(10):
#     print(number)

# for n in range (0, 20, 2):
#     print(n)

# for n in range (20, 10, -2):
#     print(n)

# for n in range(100):
#     if n % 8 == 0:
#         print(n)

new_string = ''

"""
for letter in text:
    if letter =='t':
        new_string = new_string + letter.upper()
    elif letter =='h':
        new_string += letter.upper()  # Outra forma de se fazer
    else:
        new_string += letter
print(new_string)
"""

# continue - pula para o próximo laço
#break - termina o laço

"""
for letter in text:
    if letter =='t':
        continue
        new_string = new_string + letter.upper()
    elif letter =='h':
        new_string += letter.upper()  # Outra forma de se fazer
    else:
        new_string += letter
print(new_string)
"""

for letter in text:
    if letter =='t':
        new_string = new_string + letter.upper()
    elif letter =='h':
        new_string += letter.upper()  # Outra forma de se fazer
        break
    else:
        new_string += letter
print(new_string)
