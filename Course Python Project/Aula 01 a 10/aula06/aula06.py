# Esta aula é sobre variáveis

"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Bruno'  # Igual é um operador de atribuição
print(nome)
print(nome, type(nome))

print('----'*10)

nome = 'Bruno Alves Comitre'  # str
idade = 25  # int
altura = 1.83  # float
e_maior = idade > 18  # bool
peso = 80  # int
# data_1 = True  # bool
# data_atual = 2019  # int

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print('----'*10)

print(idade * altura)

# Exercicio
# Calcular o índice de massa corporal

# Divide-se o peso do paciente pela sua altura elevada ao quadrado
imc = peso / (altura ** 2)
print('O', nome, 'tem', idade, 'anos de idade, e seu IMC é:', imc)
