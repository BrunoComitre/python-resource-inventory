# *args **kwargs

def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
func(1, 2, 3, 4, 5, nome='Python', a6=6)


def function(*args):
    print(args)
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
function(*lista, *lista2)


def funct(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['var']) 
    nome = kwargs.get('var')
    print(nome)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
funct(*lista, *lista2, var='Python')


variavel = 'valor'
def funcao():
    print(variavel)
def funcao2():
    global variavel
    variavel = 'outro valor'
    print(variavel)
def funcao3(arg=None):
    arg = arg.replace('a', 'á')
    return arg
funcao()
funcao2()
print(variavel)
outra_variavel = funcao3(arg=variavel)
print(outra_variavel)


vari = 'resultado'
def funca():
    outra_vari = 'outro resultado'
    # vari = 'outro resultado'
    # print(vari)
    return outra_vari
def funca2(arg):
    print(arg)
varia = funca()
funca2(varia)
