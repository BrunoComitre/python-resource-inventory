# Methods

def hi(obj) -> object:
    print('Hi, I`m ' + obj.name + '!')

class Robot:
    pass

x = Robot()
x.name = 'Marvin'
hi(x)

print('**************************')

# We will now bind the function ,hello" to a class attribute ,say_hi"!

def hello(obj):
        print("Hello, I am " + obj.name)

class Roboto:
    say_hi = hello

x1 = Roboto()

x1.name = "Calvin"
Roboto.say_hi(x1)

print('**************************')

# Method __init__

class A:
    def __init__(self):
        print('__init__ was execute')

x2 = A()

# We add an __init__-method to our robot class:

class Roboti:
    def __init__(self, name = None):
        self.name = name

    def say_hello(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

x3 = Roboti()
x3.say_hello()

y3 = Roboti('Balvin')
y3.say_hello()
