# EWsta aula é sobre operadores lógicos

"""
Operadores Lógicos - Aula 12
and     - e           - compara 2 coisas     - 2 == 2 and 2 < 3
or      - ou          - compara 2 coisas     - 2 == 2 or 2 < 3
not     - não         - inverte a comparação - not 2 == 2 and not 2 < 3
in      - está em     - existe em            - if 'u' in 'Bruno'
not in  - não em      - não existe em        - if 'u' not in 'Bruno'   
"""
a = 2
b = 2
c = 3
nome = 'Bruno Alves Comitre'

print('------')
print(a == b and b < c)  # (Verdadeiro E Verdadeiro) = Verdadeiro - (Verdadeiro E Falso) = Falso - Precisa das duas para retornar verdadeira

print('------')
print(a == a or b < c)  # Verdadeiro OU Verdadeiro - Precisa retornar apenas uma para ser verdadeiro

print('------')
if not a > c:
    print('C é maior que A')
else:
    print('A é maior que C')

print('------')
# if 'u' in nome:
#    print('Existe a Letra U no seu nome')

if 'Com' in nome:
    print('Existe')
else:
    print('Não Existe')

print('------')
if 'yes' not in nome:
    print('Executei')
else:
    print('Existe o texto')

# Programa de senha

usuario = input('Nome do Usuário: ')
senha = input('Senha do Usuário: ')

usuario_bd = 'Bruno'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou Senha Inválidos')
