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
