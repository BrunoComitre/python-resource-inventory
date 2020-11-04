# https://rszalski.github.io/magicmethods/

class A:
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls)
    #     return object.__new__(cls)
    
    def __new__(cls, *args, **kwargs):
        print('Método new foi chamado')

        ## SINGLETON
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    def __call__(self, *args, **kwargs):  # pode usar a classe como uma função, uma funcionalidade a mais na classe
        return f'Argumentos enviados: {args} {kwargs}'

    def __len__(self):
        return 55

    def __init__(self, nome=None):
        print('INIT')

    def __str__(self):
        return f'O que quero exibir quando essa classe se transformar em uma str'

    def __del__(self):
        print('Objeto coletado.')

    def __setattr__(self, key, value):  # é chamado toda vez que você configura um atributo na classe
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


a = A('luiz otávio')
print(type(a))
a.nome = 'luiz otávio'
a.valor = 256
print(a.nome, a.valor)
print(a)
print(len(a))
