# Esta aula é sobre formatação de string

# Exemplo da aula anterior

nome = 'Bruno Alves Comitre'  # str
idade = 25  # int
altura = 1.83  # float
e_maior = idade > 18  # bool
peso = 80  # int

imc = peso / (altura ** 2)
print('O', nome, 'tem', idade, 'anos de idade, e seu IMC é:', imc)

print('----' * 20)

print(f'Utilizando f strings')  # O f é a string de formatação da aula de hoje

print(f'O {nome} tem {idade} anos de idade, e seu IMC é: {imc}')
print(f'O {nome} tem {idade} anos de idade, e seu IMC é: {imc:.2f}')  # Arredondando o valor

print('----' * 20)

print('O {} tem {} anos de idade, e seu IMC é: {}'.format(nome, idade, imc))  # outra forma de exibir usando o format
print('O {} tem {} anos de idade, e seu IMC é: {:.2f}'.format(nome, idade, imc))  # Arredondando o valor

print('----' * 20)

# Outras formas de printar a saída

print('O {0} tem {1} anos de idade, e seu IMC é: {2}'.format(nome, idade, imc))
print('O {1} tem {2} anos de idade, e seu IMC é: {0}'.format(nome, idade, imc))

print('O {n} tem {i} anos de idade, e seu IMC é: {im}'.format(n=nome, i=idade, im=imc))
print('O {i} tem {im} anos de idade, e seu IMC é: {n}'.format(n=nome, i=idade, im=imc))
