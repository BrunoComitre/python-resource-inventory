from typing import Union, Optional
import constants as const


items = Items(items = {})
items = const.items

class Notas():

    def value(item):
        if isinstance(item, str):
            print(item.upper())
        else:
            print(str(item) + '%')
        return item

    # Use Opcional[] para valores que podem ser None
    x: Optional[str] = value(item=0)

    # Mypy entende que um valor não pode ser Nenhum em uma declaração if
    if x is not None:
        print(x)
    else:
        print('VAZIO')

    # Se um valor nunca puder ser Nenhum devido a alguns invariantes, use uma declaração
    # assert x not in None
    # print(f'ASSERT : {x}')
