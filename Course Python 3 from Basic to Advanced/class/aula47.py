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
