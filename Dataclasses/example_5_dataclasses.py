# Using Dataclasses
from dataclasses import dataclass
from typing import Dict


# Simple Mode
@dataclass
class People_Example:
    name: str
    last_name: str
    telephone: Dict[str, str]
    ddd: int

# Super Mode
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class People:
    name: str
    last_name: str
    telephone: Dict[str, str]
    ddd: int
    full_name = str = None

    def __post_init__(self):  # Executed after class initialization
        self.full_name = f'{self.name} {self.last_name}'


osterman_1 = People('Jonathan', 'Osterman', {'residential': '6666-6666', 'mobile': '666-666-666'}, 66)
osterman_2 = People('Jonathan', 'Osterman', {'residential': '6666-6666', 'mobile': '666-666-666'}, 66)
kovacs = People('Walter', 'Kovacs', {'residential': '7777-7777', 'mobile': '777-777-777'}, 77)

print(osterman_1 == osterman_2)

print(kovacs)

print(kovacs.name)

print(kovacs.telephone)
