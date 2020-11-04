# HERANÇA SIMPLES

"""
Associação - Usa | Agregação- Tem | Composição - É Dono | Herança - É  
"""

from classes import *

cliente1 = Cliente('João', 38)
print(cliente1.nome)
cliente1.falar()
cliente1.comprar()
print()

aluno1 = Aluno('Maria', 26)
print(aluno1.nome)
aluno1.falar()
aluno1.estudar()
print()

cliente2 = ClienteVIP('José', 58, "Silva")
print(cliente2.nome)
print(cliente2.sobrenome)
cliente2.falar()
cliente2.comprar()
cliente2.vip()
print()
