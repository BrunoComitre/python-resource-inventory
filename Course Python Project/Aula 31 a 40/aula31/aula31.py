# Esta aula é sobre funções em Python

"""
Funções - def (Parte 1)
"""

def function():
    print('Hello World!')

function()

def function(msg):
    print(msg)

function('Mensagem')

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Bruno Alves Comitre')
saudacao('Oi', 'Bruno ')
saudacao('Bom Dia', 'Alves')
saudacao('Boa Noite', 'Comitre')

def saudacao(msg = 'Olá', nome = 'Usuário'):
    print(msg, nome)

saudacao()

def saudacao(msg = 'Olá', nome = 'Usuário'):
    print(msg, nome)

saudacao(nome = 'Bruno', msg = 'Oi')

def saudacao(msg = 'Olá', nome = 'Usuário'):
    nome = nome.replace('o','3')
    msg = msg.replace('o','3')
    print(msg, nome)

saudacao(nome = 'Bruno', msg = 'oi')

def saudacao(msg = 'Olá', nome = 'Usuário'):
    nome = nome.replace('á','3')
    msg = msg.replace('á','3')
    return f'{msg} {nome}'

variavel = saudacao()
print(variavel)
