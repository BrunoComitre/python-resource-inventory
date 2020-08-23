# AULA: https://www.youtube.com/watch?v=sbCJucr8aJg

from typing import Dict, Set, List

# UNICÓRNIO
class Publicador:
    def __init__(self, topico, pub_sub):
        self.topico = topico
        self.mensagens = []
        self.pub = pub_sub

    def publicar(self, mensagem):
        msg = {'tópico': self.topico,'mensagem': mensagem}
        self.pub.receber_mensagem(msg)

# BOLA CRISTAL
class Incrito:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, topico, mensagem):
        print(f"|{tópico}| \t {self.nome} recebeu: '{mensagem}'")

# POVO PAUL
class PubSub:
    def __init__(self):
        self.inscritos_por_topico: Dict[str, Set] = {}
        self.fila_de_mensagens: List[Dict[str, str]] = []

    def adicionar_inscrito(self, topico, inscrito):
        if topico in self.inscritos_por_topico:
            self.inscritos_por_topico[topico].add(inscrito)
        else:
            self.inscritos_por_topico[topico] = (inscrito)

    def receber_mensagem(self, mensagem: Dict[str, str]):
        """"{'topico': xpto, 'mensagem': xpto}"""
        self.fila_de_mensagens.append(mensagem)

    def _enviar_mensagem_por_topico(self, topico, mensagem):
        for incrito in self.inscritos_por_topico[topico]:
            incrito.atualizar(topico, mensagem)

    def broadcast(self):
        for msg in self.fila_de_mensagens:
            self._enviar_mensagem_por_topico(msg['topico'], msg['mensagem'])

        self.fila_de_mensagens = []


# RUN

eduardo = Incrito('eduardo')
maria = Incrito('maria')
jose = Incrito('jose')

bus = PubSub()

blog_1 = Publicador('blog do ze', bus)
blog_2 = Publicador('psf', bus)

bus.adicionar_inscrito('psf', eduardo)
bus.adicionar_inscrito('blog do ze', eduardo)
bus.adicionar_inscrito('psf', maria)
bus.adicionar_inscrito('blog do ze', jose)

blog_1.publicar('zé foi a feira hoje')
blog_2.publicar('zé, membro da psf foi a feira hoje')

bus = broadcast()
