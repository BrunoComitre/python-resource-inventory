from typing import NoReturn, List
from difflib import ndiff

def file_diff(file_1: str, file_2: str) -> NoReturn:
    def read_file(file: str) -> List:
        """Abre o arquivo, ignorando a linha inicial e final."""
        return [
            e.replace(',','')
            for e in open(file).readlines()[1: -1]
            ]

    content_1 = read_file(file_1)
    content_2 = read_file(file_2)

    print(''.join(ndiff(content_1, content_2)))


print(file_diff('funcoes_Texto_1.txt','funcoes_texto_2.txt'))
