from datetime import datetime


class Pessoa:
    year = int(datetime.strftime(datetime.now(), '%Y'))
    
    def __init__(self, name, age, eat=False, speak=False):
        self.name = name
        self.age = age
        self.eat = eat
        self.speak = speak
        
        variavel = 'Valor'
        print(variavel)
    
    # def outro_metodo(self):
    #     print(variavel)
        
    # def outro_metodo(self):
    #     print(self.nome)
    
    def speaking(self, theme):
        if self.eat:
            print(f'{self.name} nao pode falar comendo.')
            return
        
        if self.speak:
            print(f'{self.name} ja esta falando.')
            return
        
        print(f'{self.name} esta falando sobre {theme}.')
        self.eat = True
        
    def stop_speaking(self):
        if not self.speak:
            print(f'{self.name} nao esta falando.')
            return

        print(f'{self.name} parou de falar.')
        self.eat = False

    def eating(self, food):
        if self.eat:
            print(f'{self.name} ja esta comendo {food}.')
            return
        
        if self.speak:
            print(f'{self.name} nao pode comer falando.')
            return

        print(f'{self.name} esta comendo {food}.')
        self.eat = True
    
    def stop_eating(self):
        if not self.eat:
            print(f'{self.name} nao esta comendo.')
            return
        
        print(f'{self.name} parou de comer.')
        self.eat = False
        
    def get_year_birthday(self):
        return self.year - self.age
