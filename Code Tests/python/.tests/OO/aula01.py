#
# Aula 01 - Programação Orientada a Objetos
#

# Criar Snippets em Python


# Métodos ñao funções internas das classe. 

# Classe é um grupo de entidades de individuos, que tem caracteristicas especificas,
# determinadas por atributos, e abstraçoes de operações são dadas por métodos 
# que fazem isso aocntecer.

# classmethod, precisa de self ou cls, pois é usado para as coisas da classe, referencia como classe,
# deixa explicito que o método é a abstração e não o conceito.

# staticmethod, não precisa de self ou cls uma vez que é interno ao método.

## ABSTRAÇAO DE DADOS

class Fila:
    """AAbstração de qualquer tipo de fila
    - supermercado
    - banco
    - loterica"""
    c_fila = []

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)

    def __init__(self):
        """Inicializador da classe."""
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)

class Pizza:
    piece = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def catch_piece(self):
        """Método de instancia."""
        self.piece -= 1

    @classmethod
    def alter_size(cls):
        cls.piece = piece
    
    

    

