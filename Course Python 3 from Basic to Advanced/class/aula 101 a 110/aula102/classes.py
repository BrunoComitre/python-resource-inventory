# HERANÇA SIMPLES

# Super Classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nome} está falando..')
        print(f'{self.nome_classe} está falando..')
        
# Sub Classe
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} está comprando..')


# Sub Classe
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} está estudando..')
    