from typing import Union, Optional

def print_nota(nota):
    if isinstance(nota, str):
        print(nota + ' porcento')
    else:
        print(str(nota) + '%')
    return nota

# Use Opcional[] para valores que podem ser None
x: Optional[str] = print_nota(2)
ou
x: Optional[str] = print_nota('Dois')
ou
x: Optional[str] = print_nota(None)

# Mypy entende que um valor não pode ser Nenhum em uma declaração if
if x is not None:
    print(x)
else:
    print('VAZIO')

# Se um valor nunca puder ser Nenhum devido a alguns invariantes, use uma declaração
# assert x not in None
# print(f'ASSERT : {x}')
