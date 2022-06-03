from ast import Call
from typing import Callable, Dict, Generator, List, Sequence, Tuple, Union


def sum_1(x: int) -> int:
    return x + 1


Alias =  Union[List[int], Dict[int, str], Tuple[int, int, int, ], str]

# def mymap(function: Callable, list_value: Sequence) -> Generator:
# def mymap(function: Callable, list_value: Union[List, Dict, Tuple]) -> Generator:
# def mymap(function: Callable, list_value: List[int]) -> Generator:
# def mymap(function: Callable, list_value: Tuple[int]) -> Generator:
# def mymap(function: Callable, list_value: Tuple[int, int, int]) -> Generator:
# def mymap(function: Callable, list_value: Dict[int, str]) -> Generator:
# def mymap(function: Callable,
#         list_value: Union[List[int], Dict[int, str], Tuple[int, int, int, ], str]) -> Generator:
def mymap(function: Callable, list_value: Alias) -> Generator:
    return (function(x) for x in list_value)

mymap(sum_1, [1, 2, 3])
mymap(sum_1, (1, 2, 3))
mymap(sum_1, 'string')
mymap(sum_1, {1: 'a', 2: 'b'})
