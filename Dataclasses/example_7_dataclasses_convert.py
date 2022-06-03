# Using Dataclasses and Fields
from dataclasses import asdict, astuple, dataclass, field
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

print(asdict(kovacs))
print()

print(astuple(kovacs))
print()

print(kovacs)
print()

# Convert data exist for dataclass
kovacs = People('Walter', 'Kovacs', 77)

walter = astuple(kovacs)
People(*walter[:-1])
print(walter)
print()

roschach = asdict(kovacs)
del roschach['full_name']
People(**roschach)
print(roschach)
print()
