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
    
    def falar(self):
        print(' Estou em cliente...')

# Sub Classe
class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        # Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
        
    def vip(self):
        print(f'{self.nome} é VIP..')
    
    def comprar(self):
        print(f'{self.nome_classe} VIP está comprando..')
    
    def falar(self):
        # super().falar()
        Pessoa.falar(self)
        print(f'{self.nome} está falando...')
        print(f'{self.nome_classe} está falando...')
        
# Sub Classe
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} está estudando..')

    def falar(self):
        super().falar()
        print(f'{self.nome} está falando...')
        print(f'{self.nome_classe} está falando...')