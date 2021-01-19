# Essa aula é sobre expressÇao condicional com OR

# EXEMPLO CONVENCIONAL
# nome = input('Qual o seu nome ?')
# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada')

# EXEMPLO OR
# nome = input('Qual o seu nome ?')
# print (nome or 'Você não digitou nada')
# print (nome or None or False or 0 or 'Você não digitou nada' or 'Outa Coisa')  # Não exibe o Outra Coisa, porque ele sempre exibe a primeira que der verdadeiro - True 

a = 0
b = None
c = False
d = []
e = {}
f = 25
g = 'Bruno'

variavel = a or b or c or d or e or f or g
print(variavel)
