# Esta aula é sobre o Desafio - Valide um CPF

"""
CPF = 168.995.350-09
------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9 = 54            #    6 * 10 = 60
8 * 8 = 64            #    8 * 9 = 72
9 * 7 = 63            #    9 * 8 = 72
9 * 6 = 54            #    9 * 7 = 63
5 * 5 = 25            #    5 * 6 = 30
3 * 4 = 12            #    3 * 5 = 15
5 * 3 = 15            #    5 * 4 = 20
0 * 2 = 0             #    0 * 3 = 0
                      # -> 0 * 2 = 0
        297           #         343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #     Digito 2 = 9
"""

cpf = '16899535005'

if len(cpf) < 11:
    print('Ele deve ter apenas 11 Números')   
    
if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
    print('Erro')
    
calc = lambda t: int(t[1]) * (t[0] + 2)
d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
resultado =  str(d1) == cpf[-2] and str(d2) == cpf[-1]
if cpf == str(d1) == cpf[-2] and str(d2) == cpf[-1]:
    print('Válido')
else:
    print('Inválido')
