# Esta aula é sobre Operação Ternária

"""
Operador Ternário
"""

# OPERAÇÃO PADRÂO
# logged_user = True
# if logged_user:  # É a mesma coisa que escrita: if logged_user == True:
#     message = 'Usuário Logado'
# else:
#     message = 'Usuário precisa Logar'
# print(message)

# UTILIZANDO OPERADOR TERNÁRIO
# logged_user = False
# message = 'Usuário Logado' if logged_user else 'Usuário precisa Logar'
# print(message)

# SABENDO SE A PESSOA É MAIOR DE IDADE
# idade = 18
# if idade >= 18:
#     print('Pode Acessar')
# else:
#     print('Não Pode Acessar')

idade = input('Digite sua idade: ')
if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    message = 'Pode Acessar' if e_de_maior else 'Não Pode Acessar'
    print(message)
