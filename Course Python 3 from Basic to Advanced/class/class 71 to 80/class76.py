
try:
    # a = []
    a = {}
    # print(a[1])
    # print(a)
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave:', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    print('Codigo executado com sucesso')
finally:
    print('Finally sempre e executado')
    print(a)

print('continua')

######################################

def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as erro:
        print(erro)
        raise
        # return False

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print('Log:', error)

######################################

def div(n1, n2):
    if n2 == 0:
        raise ValueError("n2 nao pode ser 0.")
    return n1 / n2

print(div(2, 1))

try:
    print(div(2, 0))
except ValueError as erro:
    print('Erro:', erro)

######################################

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

numero = converte_numero(input('Digite um numero: '))

if numero is not None:
    print(numero + 5)
else:
    print('Nao e numero.')
