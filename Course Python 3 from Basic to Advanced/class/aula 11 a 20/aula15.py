numero = 0

while numero <= 10:
    print(numero)
    numero += 1

while True:
    if numero <=10:
        print(numero)
    else:
        print('Não')


x = 0  # coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y+=1
        
    x +=1

contador = 1
acumulador = 1

while contador  <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador +=1
else:
    print('Cheguei')