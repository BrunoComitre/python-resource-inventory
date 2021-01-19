# Esta aula é sobre While/Else - Repetição com acumuladores

"""
While / Else
contadores
acumuladores
"""

cont = 1
acumulador = 1

while cont <= 10:
    print(cont,acumulador)

    if cont > 5:
        break

    acumulador = acumulador + cont
    cont +=1
else:
    print('Cheguei no else')

print('Esse print será executado.')  # Pois está fora do break
