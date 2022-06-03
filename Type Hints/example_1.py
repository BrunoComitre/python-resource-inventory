from typing import Any, Dict, List, NewType, Tuple, TypeVar, Union


# Example not good
def concat1(t1:[int, str, list, tuple],
           t2:[int, str, list, tuple]) -> [int, str, list, tuple]:
    return t1 + t2

print(concat1.__annotations__)
print()


# Example ok
def concat2(t1: Union[List, Tuple, int],
           t2: Union[List, Tuple, int]) -> Union[List, Tuple, int]:
    return t1 + t2

print(concat2.__annotations__)
print()


# Example best
def concat3(t1: Any, t2: Any) -> Any:
    return t1 + t2

print(concat3.__annotations__)
print()


# Just Numerics Types
def numeric_sum(x: Union[int, float, complex],
                y: Union[int, float, complex]) -> Union[int, float, complex]:
    return x + y

print(numeric_sum.__annotations__)
print()
# Return: ~Number : which means it was done by the user

# Just Numerics Types using TypeVar
Number = TypeVar('Number', int, float, complex)

def numeric_sum_new_type(x: Number, y: Number) -> Number:
    return x + y

print(numeric_sum_new_type.__annotations__)
print()


# Exemple Types using NewType and Dict
#DataRegister = NewType('Register', Dict[str, str])
# or
DataRegister = Dict[str, str]

def valid_register(user: DataRegister) -> bool:
    ...

print(valid_register.__annotations__)
print()
