from typing import Union, overload

"""
Another way to do:

overlord: overrides the function option, so if it gets int, it returns int, if
it gets str it returns str, i.e., one function overrides the other
"""

# Create by Bruno Comitre
# def sum(x: Union[int,str], y: Union[int,str]) -> Union[int,str]:
#     ...

@overload
def sum(x: int, y: int) ->int:
    ...

@overload
def sum(x: str, y: str) -> str:
    ...

@overload
def sum(x: float, y:float) -> float:
    ...

def sub(x: Union[int,str], y: Union[int,str]) -> Union[int,str]:
    ...

@overload
def mult(x: float, y: float) ->float:
    ...

@overload
def mult(x: Union[int,str], y: Union[int,str]) -> Union[int,str]:
    ...

def div(x: Union[int,str, float], y: Union[int,str, float]) -> Union[int,str, float]:
    ...

# Stub file creates by monkeytype
# def sub(x: str, y: str):
#   ...

# def sum(x: Union[int, str, float], y: Union[int, str, float]) -> Union[int, str, float]:
#   ...
