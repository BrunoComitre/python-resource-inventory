# Desempacotamento de iteráveis em Python (*args)
# https://www.youtube.com/watch?v=ztlu_oD1hLY&t=216s


# EXEMPLO SIMPLES
fullname = ('Bruce', 'Wayne')
firstname, lastname = fullname
print(f'My name is: {firstname}')
print(f'My last name is: {lastname}')
print(f'Call me by Sr. {fullname}')
# Desempacotando com exemplo acima
print(*fullname)


# EXEMPLO VÁRIOS DADOS NO ITERÁVEL
fullname = ['Batman', 'Gothan', 'Bruce', 'Wayne']
# Se eu quiser ignorar eu posso usar _
# _,firstname, lastname = fullname
# Exemplo acima daria um erro, pois tenho mais dados para desempacotar
_, _,firstname, lastname = fullname
print(f'My name is: {firstname}')
print(f'My last name is: {lastname}')
# print(_)
print(_)
print(f'Call me by Sr. {fullname}')


# EXEMPLO USANDO REST
fullname = ['Batman', 'Gothan', 'Bruce', 'Wayne']
# Esse rest, é meio que uma convenção pra entender que seria o resto daquilo que foi desempacotado
firstname, lastname, *rest = fullname
print(f'My name is: {firstname}')
print(f'My last name is: {lastname}')
print(f'And this is the: {rest}')
# Também posso desempacotar assim
print(*rest)


# UM EXEMPLO DE EMPACOTAMENTO AS É UMA MÁ PRÁTICA
a, b = 1, 2
print(f'a: {a}, b: {b}')
a, b = b, a
print(f'a: {a}, b: {b}')


# EXEMPLO DE DESEMPACOTAMENTO COM FUNÇÃO E ARGS
# ARGS E KWARGS SÃO NOMES DE CONVENÇÃO
def the_args(*args):
    first, second, *rest = args
    print(first, second)
    # print(args)
    print(*args)
    print(rest)

the_args('one', 'two', 'many', 'values')

# EXEMPLO LISTA MULTIDIMENSIONAIS
list_mult = [[1, 2], [3, 4]]
[one, two], [three, four] = list_mult
print(one, two, three, four)

# EXEMPLO COM RANGE
lista = list(range(1, 11))
print(lista)
# Como se gerasse um empacotamento
lista_empac = [range(1, 11)]
print(lista_empac)
# Funciona com range, um desempacotamento
lista_empac2 = [*range(1, 11)]
print(lista_empac2)
