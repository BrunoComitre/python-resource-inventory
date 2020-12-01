"""
Descrição rápida e simples

Esta é uma descrição de
documentação de funções em Python

Documentação referente ao módulo
"""

from abc import abstractmethod

class MinhaClasse:
    """Documentação da classe
    Podendo conter várias linhas
    """
    atributo = 1
    atributo2 = 'Valor'
    
    def __init__(self, texto) -> None:
        """ Inicializa os dados
        
        :param texto: o texto da classe
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto = (texto)
        
        @abstractmethod
        def exibe_texto(texto):
            """ Método que exibe um texto de 100 caracteres na tela
            
            :param texto: Um texto de 100 caracteres
            :type texto: str
            
            :return: O texto de 100 caracteres
            :rtype: str
            
            :raises ValueError: Se o texto tiver mais de 100 caracteres
            :raises TypeError: Se o texto não for uma string
            """
            if not isinstance(texto, str):
                raise TypeError('O texto precisar ser uma string')
            
            if len(texto) > 100:
                raise ValueError('O texto precisar ter 100 caracteres ou menos')
            
            return texto
