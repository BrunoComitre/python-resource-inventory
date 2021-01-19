# Esta aula é sobre funções - CONTINUAÇÃO

"""
Funções (def) - *args **kwargs - (Parte 3)
"""

"""
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)
"""

# Se você nâo sabe quantos argumentos vai vir na sua função, você utiliza o *args

def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    print(nome)

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]
func(*lista_1, *lista_2, nome='Bruno', sobrenome='Alves')

# **kwargs - keywords argumentos
