def test(x, y):
    resultado = x + y
    return f'{resultado}'
variavel = test(2,5)
print(variavel)


def divisao(x, y):
    if y == 0:
        return
    return x / y
divide = divisao(8,2)
if divide:
    print(divide)
else:
    print('conta inválida')


def saudacao(x, y):
    return f'{x}, {y}'
saudacoes = saudacao('Olá','Python')
print(saudacoes)


def soma(x, y, z):
    if y == 0:
        return
    return x + y + z
conta = soma(1, 2, 3)
print(conta)


def percentual(x, y):
    if y == 0:
        return
    return x + (y * x / 100)
resultado = percentual(100, 10)
print(resultado)

def fizzbuzz(x):
    if x % 2 == 0:
        return f'fizz'
    elif x % 5 == 0 or x % 3 == 0:
        return f'fizzbuzz'
    return x

valor = fizzbuzz(2)
print(valor)
valor = fizzbuzz(5)
print(valor)
valor = fizzbuzz(3)
print(valor)
valor = fizzbuzz(349)
print(valor)
