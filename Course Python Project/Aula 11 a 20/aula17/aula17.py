# Essa aula é sobre iterar strings

"""
Iterando strings com While
"""

string = 'o rato roeu a roupa do rei de roma.'

cont = 0

new_string = ''

# print(string.count('a'))

"""
while cont < len(string):

    if string[cont] == 'r':
        new_string = new_string + string[cont].upper()
    else:
        new_string = new_string + string[cont]

#    print(cont, string[cont])

    cont += 1

print(new_string)
"""

while True:
    string = str(input('Digite uma Frase: '))
    cont = 0
    new_string = ''
    contagem = 0
    letra = ''

    while cont < len(string):
        conta = string.count(string[cont])

        if contagem < conta and string[cont].strip():
            letra = string[cont]
            contagem = conta

    #    print(string[cont],conta)
        cont += 1

    print(letra, contagem)
