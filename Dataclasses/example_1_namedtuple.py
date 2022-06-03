# No Typing
from collections import namedtuple

person = namedtuple('Person', 'name last_name telephone ddd')

data = [
    person('Bruce', 'Wayne', {'residential': '1111-1111', 'mobile': '111-111-111'}, 11),
    person('Barry', 'Allen', {'residential': '2222-2222', 'mobile': '222-222-222'}, 22),
]

bruce = data[0]
bruce = person('Bruce', 'Wayne', {'residential': '1111-1111', 'mobile': '111-111-111'}, 11)

bruce.name
bruce.last_name
bruce.telephone
bruce.ddd
