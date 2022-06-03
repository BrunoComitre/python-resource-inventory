# With Typing
from typing import Dict, NamedTuple


class People(NamedTuple):
    name: str
    last_name: str
    telephone: Dict[str, str]
    ddd: int


wick = People('John', 'Wick', {'residential': '3333-3333', 'mobile': '333-333-333'}, 33)

wick.name
wick.last_name
wick.telephone
wick.ddd
