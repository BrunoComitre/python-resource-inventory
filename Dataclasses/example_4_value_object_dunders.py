# Using Value Object Pattern
from typing import Dict


class People:
    def __init__(self, name: str, last_name: str, telephone: Dict[str, str], ddd: int):
        self.name = name
        self.last_name = last_name
        self.telephone = telephone
        self.ddd = ddd

# dunder __eq__ : how to compare two equal objects
    def __eq__(self, _o) -> bool:  # _o means other
        return all ([
            self.name == _o.name,
            self.last_name == _o.last_name,
            self.telephone == _o.telephone,
            self.ddd == _o.ddd
        ])

# dunder __repr__ : how it will be printed on the screen
    def __repr__(self) -> str:
        return f'People({self.name},{self.last_name}, {self.telephone}, {self.ddd})'


osterman_1 = People('Jonathan', 'Osterman', {'residential': '6666-6666', 'mobile': '666-666-666'}, 66)
osterman_2 = People('Jonathan', 'Osterman', {'residential': '6666-6666', 'mobile': '666-666-666'}, 66)
kovacs = People('Walter', 'Kovacs', {'residential': '7777-7777', 'mobile': '777-777-777'}, 77)

print(osterman_1 == osterman_2)

print(kovacs)
