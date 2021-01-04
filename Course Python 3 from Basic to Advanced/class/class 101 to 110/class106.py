"""
Polimorfismo é o principio que permite que as classes derivadas de uma mesma
suérclasse tenham métodos iguais (de mesma assinatura) mas comportamentos
diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""
"""
Comparação arquivos aula 105

Assinaturas do método sacar. Onde cada classe tem a mesma assinatura (sacar) = mas
tem escritas/comportamentos diferentes.
"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):  # mesma assinatura de A
        print(f'B está falando {msg}')  # comportamento diferente


class C(A):
    def fala(self, msg):  # mesma assinatura de A
        print(f'C está falando {msg}')  # comportamento diferente

b = B()
c = C()

b.fala('UM ASSUNTO')
c.fala('OUTRO ASSUNTO')
