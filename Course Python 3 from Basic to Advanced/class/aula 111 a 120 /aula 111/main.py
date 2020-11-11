"""
Animal -> respirar (é um Animal)
    Lobo(Animal) -> respirar / uivar (Lobo é um lobo e um Animal)
    Cachorro(Lobo) -> respirar / uivar / latir (cachorro é um Cachorro, também é um lobo() e um Animal())
"""

from classes.interface import Interface


interface1 = Interface()
interface1.metodo_da_interface()
