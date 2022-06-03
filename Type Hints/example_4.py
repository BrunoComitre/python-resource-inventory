"""
using : my_lib.py and my_lib.pyi

pyi : it is a file stub

run : monkeytype run exemplo_4, generates file : moneytype.sqlite3

run : monkeytype stub my_lib

run : monkeytype stub my_lib > stub.pyi : generates file with all types

run : monkeytype apply my_lib : send all types to file overwrites my_lib and you
can run : monkeytype stub my_lib > my_lib.pyi, to send correct file stub, to
separate type to file

"""

from my_lib import div, mult, sub, sum

sum('str', 'str')
sum(1, 1)
sum(1.0, 1.0)

sub('str', 'str')
sub(1, 1)

mult('str', 'str')
mult(1, 1)
mult(1.0, 1.0)

div('str', 'str')
div(1, 1)
div(1.0, 1.0)
