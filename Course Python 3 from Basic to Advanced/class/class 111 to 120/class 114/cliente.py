"""
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
"""

from conta import ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str):
            raise ValueError("Nome precisa ser uma String")

        self._nome = valor

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Idade precisa ser numérico")

        self._idade = valor
        
class Cliente:
    pass