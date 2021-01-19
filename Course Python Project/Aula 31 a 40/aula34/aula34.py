# Esta aula é sobre funções - CONTINUAÇÃO

"""
Funções (def) - Escopo de Variáveis - (Parte 4)
"""

# Variável de escopo global, significa que a variável está acessível em toda parte da aplicação

"""
variavel = 'Valor'

def func():
    print(variavel)

def func2():
    variavel = 'Outro Valor'
    print(variavel)

func()
func2()

print(variavel)
"""

variavel = 'Valor'

def func():
    print(variavel)

def func2():
    global variavel
    variavel = 'Outro Valor'
    print(variavel)

func()
func2()

print(variavel)
