# Este é um Desafio Prático

"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com chaves)
"""

nome = 'Bruno Alves Comitre'
idade = 25
altura = 1.83
peso = 80.0
ano_atual = 2019
data_de_nascimento = (ano_atual - idade)
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura}m de altura e pesa {80}Kg. \nO IMC de {nome} é {imc:.2f}. \n{nome} nasceu em {data_de_nascimento}.')
