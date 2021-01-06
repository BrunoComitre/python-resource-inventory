def resultado():
    return 'Resultado'

def mestre(funcao):
    return funcao()

executando  = mestre(resultado)
print(executando)


def mestre_dois(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'
    
executando = mestre_dois(oi, 'Python')
executando2 = mestre_dois(saudacao, 'Python', saudacao='Olá')
print(executando)
print(executando2)
