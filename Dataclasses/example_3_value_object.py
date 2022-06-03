# Using Value Object Pattern
from typing import Dict


class People:
    def __init__(self, name: str, last_name: str, telephone: Dict[str, str], ddd: int):
        self.name = name
        self.last_name = last_name
        self.telephone = telephone
        self.ddd = ddd


cena_1 = People('John', 'Cena', {'residential': '4444-4444', 'mobile': '444-444-444'}, 44)
cena_2 = People('John', 'Cena', {'residential': '4444-4444', 'mobile': '444-444-444'}, 44)
strange = People('Stephen', 'Strange', {'residential': '5555-5555', 'mobile': '555-555-555'}, 55)

print(cena_1 == cena_2)

print(strange)
