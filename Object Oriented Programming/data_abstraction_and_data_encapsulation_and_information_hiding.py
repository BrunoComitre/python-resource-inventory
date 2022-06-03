# Data Abstraction, Data Encapsulation, and Information Hiding

# Getter and Setter

class Robot:
    def __init__(self, name = None, build_year = None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print('Hi, I am', self.name)
        else:
            print('Hi, I am a robot without a name')
        if self.build_year:
            print('I was built in', str(self.build_year))
        else:
            print('I have no build year')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, build_year):
        self.build_year = build_year

    def get_build_year(self):
        return self.build_year


x = Robot()

x.set_name('Marvin')

x.say_hi()

y = Robot()

y.set_name(x.get_name())

print(y.get_name())

print('**************************')

x1 = Robot('Calvin', 2020)
y1 = Robot()

y1.set_name('Balvin')

x1.say_hi()

y1.say_hi()

print('**************************')

# __str__ and __repr__


l  =  ["Python", "Java", "C ++", "Perl"]

print(l)

print(str (l))

print(repr (l))

d  =  { "a" : 3497 ,  "b" : 8011 ,  "c" : 8300 }

print(d)

print(str(d))

print(repr(d))

x2 = 587,78

print(str(x2))

print(repr(x2))


class A:
    pass

a = A()

print(a)

print(repr(a))

print(str(a))

class B:
    def __str__(self):
        return "42"

b = B()

print(repr(b))

print(str(b))

class C:
    def __repr__(self):
        return "42"
c  = C()

print(repr(c))

print(str(c))


# print(o == eval(repr(o)))  # True

l = [3, 8, 9]

s = repr(l)

print(s)

print(l  ==  eval(s))

print(l  ==  eval(str(l)))

print('**************************')

import datetime

today = datetime.datetime.now()

str_s = str(today)

# print(eval(str_s)) # SyntaxError: invalid syntax. Perhaps you forgot a comma?

repr_s = repr(today)

t = eval(repr_s)

print(type(t))


class Roboto:
    def __init__(self, name = None, build_year = None):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return f'Roboto({self.name}, {self.build_year})'

    def __str__(self):
        return f'Roboto: {self.name} Build Year: str({self.build_year})'


x4 = Roboto("Marvin", 1979)
x_str = str(x4)

print(x_str)
print("Type of x_str: ", type(x_str))
# print(eval(x_str))
# print("Type of new:", type(eval(x_str)))


class Roboti:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return f'Roboti({self.name}, str({self.build_year}))'

    def __str__(self):
        return f'Name: {self.name} Build Year: str({self.build_year})'

x5 = Roboti("Marvin", 1979)
x_repr = repr(x5)

print(x_repr)
print("Type of x_str: ", type(x_repr))
# print(eval(x_repr))
# print("Type of new:", type(eval(x_repr)))
