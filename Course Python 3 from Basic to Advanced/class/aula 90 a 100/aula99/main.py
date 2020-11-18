# Assosiação

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


# escritor = Escritor('Joãozinho')
# print(escritor.nome)
# caneta = Caneta('Bic')
# print(caneta.marca)
# maquina = MaquinaDeEscrever()
# print(maquina.escrever)

# escritor.ferramenta = maquina
# escritor.ferramenta.escrever()

# del escritor
# print(caneta.marca)
# maquina.escrever()

escritor = Escritor('Joãozinho')
print(escritor.nome)
caneta = Caneta('Bic')
print(caneta.marca)
maquina = MaquinaDeEscrever()
print(maquina.escrever)

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
