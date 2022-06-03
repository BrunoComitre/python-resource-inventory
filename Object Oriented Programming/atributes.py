import math

print(type(math))

print('**************************')

# Minimal class in Python

class Robot:
    pass

if __name__ == '__main__':
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y is y2)
    print(y == x)

print('**************************')

# Atributes

class Roboto:
    pass

x1 = Roboto()
y1 = Roboto()

x1.name = 'Marvin'
x1.build_year = 1979

y1.name = 'Calvin'
y1.build_year = 1991

print(x1.name)
print(y1.build_year)

print(x1.__dict__)
print(y1.__dict__)

# Attributes can be bound to class names as well. In this case, each instance
# will possess this name as well. Watch out, what happens, if you assign the
# same name to an instance:

class Roboti(object):
    pass

x2 = Roboti()

Roboti.brand = 'Toshiba'
print(x2.brand)

x2.brand = 'Dell'
print(Roboti.brand)

y2 = Roboti()
y2.brand


Robot.brand = "Thales"
print(y2.brand)

print(x2.brand)

print(x2.__dict__)

print(y2.__dict__)

print(Roboti.__dict__)

# print(x2.energy)  # AttributeError: 'Roboti' object has no attribute 'energy'

print(getattr(x2, 'energy', 100))


def f(x) -> int:
    return 42

f.x = 42
print(f.x)

def f(x):
    f.counter = getattr(f, 'counter', 0) + 1
    return 'Monty Python'

for i in range(10):
    print(f(i))

print(f.counter)
