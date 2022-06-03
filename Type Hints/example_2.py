from typing import Optional, Union

"""
run: mypy example_2.py
"""

# '1' + 1
# 1 + 1



def sum(x: int, y):
    return x + y

sum('x', 'y')
sum(1, 2)
sum(1.0, 1.0)


def mult(x: Union[int, float], y):
    return x * y

mult('x', 'y')
mult(1, 2)
mult(1.0, 1.0)

def sub(x: Union[str, float], y: Union[int, float])-> Optional[float]:
    if isinstance(x, str):
        return None
    return x - y

sub('1', 1)
sub(1, 2)
sub(1.0, 1.0)
