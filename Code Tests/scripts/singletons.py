# TUTORIAL DE : https://cosmiccoding.com.au/tutorials/simple_singletons

########################## One Line Python Singletons ##########################

# PARTE I
class Singleton():
    def __init__(self):
        self.state = "I am Alive!"
    def set_state(self, state):
        self.state = state
    def get_state(self):
        return self.state


def function_A():
    s = Singleton()
    s.set_state("I was asked for in FUNCTION A")
    return s

def function_B():
    s = Singleton()
    s.set_state("I was asked for in FUNCTION B")
    return s

s1 = function_A()
s2 = function_B()
print([s1.state, s2.state])


# PARTE II
from functools import lru_cache

@lru_cache(maxsize=1)
def singleton_factory():
    return Singleton()

def function_C():
    s = singleton_factory()
    s.set_state("I was asked for in FUNCTION C")
    return s

def function_D():
    s = singleton_factory()
    s.set_state("I was asked for in FUNCTION D")
    return s

s3 = function_C()
s4 = function_D()
print([s3.state, s4.state])


# PARTE III
@lru_cache(maxsize=2)
def double(x):
    print(f"I am doubling {x}")
    return 2 * x

inputs = [1, 1, 2, 3, 1]
for i in inputs:
    print(double(i))
 