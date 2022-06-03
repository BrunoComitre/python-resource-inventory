# Using Dataclasses and Fields
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class People:
    name: str
    last_name: str
    ddd: int = field(repr=False)
    telephone: Dict[str, str] = field(default_factory=dict)
    full_name: str = field(init=False)

    def __post_init__(self):  # Executed after class initialization
        self.full_name = f'{self.name} {self.last_name}'


kovacs = People('Walter', 'Kovacs', 77)

kovacs.telephone |= {'mobile': '777-777-777'}

print(kovacs)

print(kovacs.name)

print(kovacs.telephone)
