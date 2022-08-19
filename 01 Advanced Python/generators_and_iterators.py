# https://python-course.eu/advanced-python/generators-iterators.php

"""
Generators are a special kind of function, which enable us to implement or generate iterators.

Mostly, iterators are implicitly used, like in the for-loop of Python.

"""

# An list is not an iterator, but can be used as an iterable
import random
from itertools import permutations
from random import choice
from typing import Generator

cities = ['Sorocaba', 'São Paulo', 'Rio de Janeiro', 'Belo Horizonte',
          'Salvador', 'Brasília', 'Minas Gerais', 'Fortaleza']

for location in cities:
    print(f'Location: {location}')

# Call next and iter

expertises = ["Python Begginer", "Python Intermediate", "Python Proficient",
              "Python Advanced", "Python Expert"]

expertises_iterator = iter(expertises)

print(f'Call "next" for the first time: {next(expertises_iterator)}')
print(f'Call "next" for the second time: {next(expertises_iterator)}')

# Simulate a loop with StopIteration

other_cities = ['Presidente Bernardes', 'Maranhão', 'Votorantim', 'Recife',
                'Belém', 'Pernambuco', 'Cuiabá', 'Manaus']

city_iterator = iter(other_cities)

while city_iterator:
    try:
        print(f'Location: {next(city_iterator)}')
    except StopIteration:
        break

# Dictionary is an iterable

capitals = {'Brazil': 'Brasília', 'Argentina': 'Buenos Aires',
            'França': 'Paris', 'Holanda': 'Amsterdã', 'Alemanha': 'Berlim',
            'Suíça': 'Bern',  'Áustria': 'Viena'}

for country in capitals:
    print(f'Capital of {country}: {capitals[country]}')

# Implements an iterator with a Class


class Cycle(object):
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.iterator_obj = iter(iterable)

    def __iter__(self) -> object:
        return self

    def __next__(self) -> object:
        while True:
            try:
                return next(self.iterator_obj)
            except StopIteration:
                self.iterator_obj = iter(self.iterable)
                return next(self.iterator_obj)


x = Cycle(["abc", "def", "ghi"])
for i in range(10):
    print(next(x), end=", ")

# Implements an iterator with a Generator (THE PYTHONIC WAY)


def city_generator():
    yield("Hamburg")
    yield("Konstanz")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")  # This is the last element


city = city_generator()
print(f'First element: {next(city)}')
print(f'Second element: {next(city)}')
print(f'Third element: {next(city)}')
print(f'Fourth element: {next(city)}')
print(f'Fifth element: {next(city)}')
print(f'Sixth element: {next(city)}')
# print(f'Seventh element: {next(city)}')  # This will raise an error

# Method Of Operation

"""
Method of working:

- A generator is called like a function. Its return value is an iterator, i.e. a
  generator object. The code of the generator will not be executed at this stage
- The iterator can be used by calling the next method. The first time the
  execution starts like a function, i.e. the first line of code within the body
  of the iterator. The code is executed until a yield statement is reached
- yield returns the value of the expression, which is following the keyword
  yield. This is like a function, but Python keeps track of the position of
  this yield and the state of the local variables is stored for the next call.
  At the next call, the execution continues with the statement following the
  yield statement and the variables have the same values as they had in the
  previous call.
- The iterator is finished, if the generator body is completely worked through
  or if the program flow encounters a return statement without a value.
"""


def counter_current(firstval=0, step=1):
    current = firstval
    while True:
        yield current
        current += step


counter = counter_current()

for i in range(10):
    print(next(counter), end=", ")
    print(type(counter))

start_value = 2.1
stop_value = 0.3

print('\n\nNew Counter value:')

counter = counter_current(start_value, stop_value)

for i in range(10):
    new_value = next(counter)
    print(f'{new_value:2.2f}', end=", ")
    print(type(new_value))

# Fibonacci Sequence as an Generator


def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)

for x in f:
    print(x, " ", end="")
print()


def fibonacci_infinite():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci_infinite()

counter = 0

for x in f:
    print(x, " ", end="")
    counter += 1
    if (counter > 10):
        break
print()

# Using a 'return' in to a Generator


def generator() -> Generator:
    yield 1
    # raise StopIteration(42) # This will stop the generator
    yield 2


# g = generator()

# next(g)

# next(g)


def generator_return() -> Generator:
    yield 1
    # return 42 # This will stop the generator
    yield 2


# gr = generator_return()

# next(gr)

# next(gr)

# Send Methods / Coroutines


def simple_coroutine():
    print('-> coroutine started!')
    x = yield "foo"
    print(f'-> coroutine received: {x}')


# cr = simple_coroutine()
# print(cr)

# next(cr)

# return_value = cr.send  # ("bar")
# print(f'-> coroutine send return: {return_value}') # This will raise an error

# Another Example for Send


def song_gen(song_list):
    new_song = None
    while True:
        if new_song != None and new_song not in song_list:
            song_list.append(new_song)
            new_song = yield new_song
        else:
            new_song = yield(choice(song_list))


songs = ["Her Şeyi Yak - Sezen Aksu",
         "Bluesette - Toots Thielemans",
         "Six Marimbas - Steve Reich",
         "Riverside - Agnes Obel",
         "Not for Radio - Nas",
         "What's going on - Taste",
         "On Stream - Nils Petter Molvær",
         "La' Inta Habibi - Fayrouz",
         "Ik Leef Niet Meer Voor Jou - Marco Borsato",
         "Δέκα λεπτά - Αθηνά Ανδρεάδη"]

radio_program = song_gen(songs)

next(radio_program)

for i in range(3):
    print(next(radio_program))

radio_program.send("Distorted Angels - Archive")

print(songs)

# Send with new musics


def song_generator(song_list):
    new_song = None
    while True:
        if new_song != None:
            if new_song[0] == "-songlist-":
                song_list = new_song[1]
                new_song = yield(choice(song_list))
            else:
                title, performer = new_song
                new_song = title + " - " + performer
                if new_song not in song_list:
                    song_list.append(new_song)
                new_song = yield new_song
        else:
            new_song = yield(choice(song_list))


songs1 = ["Après un Rêve - Gabriel Fauré"
          "On Stream - Nils Petter Molvær",
          "Der Wanderer Michael - Michael Wollny",
          "Les barricades mystérieuses - Barbara Thompson",
          "Monday - Ludovico Einaudi"]

songs2 = ["Dünyadan Uszak - Pinhani",
          "Again - Archive",
          "If I had a Hear - Fever Ray"
          "Every you, every me - Placebo",
          "Familiar - Angnes Obel"]

radio_prog = song_generator(songs1)

for i in range(5):
    print(next(radio_prog))

radio_prog.send(("-songlist-", songs2))

for i in range(5):
    print(next(radio_prog))

# The throw Method


def counter_gen(firstval=0, step=1):
    counter = firstval
    while True:
        try:
            new_counter_value = yield counter
            if new_counter_value is not None:
                counter += step
            else:
                counter = new_counter_value
        except Exception:
            yield (firstval, step, counter)


c = counter_gen()

for i in range(6):
    print(next(c))

print("Let us see what the state of the iterator is:")

state_of_count = c.throw(Exception)

print(state_of_count)

print("now, we can continue:")

for i in range(3):
    print(next(c))

# We can improve the previous example by defining our own exception class StateOfGenerator:


class StateOfGenerator(Exception):
    def __init__(self, message=None):
        self.message = message


def count(firstval=0, step=1):
    counter = firstval
    while True:
        try:
            new_counter_val = yield counter
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val
        except StateOfGenerator:
            yield (firstval, step, counter)


c = count()

for i in range(3):
    print(next(c))

print("Let us see what the state of the iterator is:")

i = c.throw(StateOfGenerator)

print(i)

print("now, we can continue:")

for i in range(3):
    print(next(c))

# yield from


def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i


def gen2():
    yield from "Python"
    yield from range(5)


g1 = gen1()

g2 = gen2()

print("g1: ", end=", ")

for x in g1:
    print(x, end=", ")

print("\ng2: ", end=", ")

for x in g2:
    print(x, end=", ")
print()


def cities():
    for city in ["Sorocaba", "São Paulo", "Belém", "Votorantim"]:
        yield city


def squares():
    for number in range(10):
        yield number ** 2


def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number


def generator_splitted():
    yield from cities()
    yield from squares()


lst1 = [el for el in generator_all_in_one()]

lst2 = [el for el in generator_splitted()]

print(lst1 == lst2)


def subgenerator():
    yield 1
    return 42


def delegating_generator():
    x = yield from subgenerator()
    print(x)


for x in delegating_generator():
    print(x)

"""
The full semantics of the yield from expression is described in six points in
"PEP 380 -- Syntax for Delegating to a Subgenerator" in terms of the
generator protocol:

- ny values that the iterator yields are passed directly to the caller.
- Any values sent to the delegating generator using send() are passed directly
  to the iterator. If the sent value is None, the iterator's next() method is
  called. If the sent value is not None, the iterator's send() method is
  called. If the call raises StopIteration, the delegating generator is
  resumed. Any other exception is propagated to the delegating generator.
- Exceptions other than GeneratorExit thrown into the delegating generator are
  passed to the throw() method of the iterator. If the call raises
  StopIteration, the delegating generator is resumed. Any other exception is
  propagated to the delegating generator.
- If a GeneratorExit exception is thrown into the delegating generator, or the
  close() method of the delegating generator is called, then the close() method
  of the iterator is called if it has one. If this call results in an exception,
  it is propagated to the delegating generator. Otherwise, GeneratorExit is
  raised in the delegating generator.
- The value of the yield from expression is the first argument to the
  StopIteration exception raised by the iterator when it terminates.
- return expr in a generator causes StopIteration(expr) to be raised upon exit
  from the generator.
"""

# Recursive Generators

"""
Permutation:

Is a rearrangement of the elements of an ordered list. In other words:
Every arrangement of n elements is called a permutation.

In the following lines we show all the permutations of the letter a, b and c:

a b c
a c b
b a c
b c a
c a b
c b a
"""


def permutations(items):
    n = len(items)
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i] + items[i + 1:]):
                yield [items[i]] + cc


for p in permutations(['r', 'e', 'd']):
    print(''.join(p))

for p in permutations(list("game")):
    print(''.join(p) + ", ", end="")

# Creating Permutations using itertools.permutations


perms = permutations(['f', 'o', 'o'])
print(list(perms))

"""
Permutations can denote in this weaker meaning a sequence of elements, where
each element occurs just once, but without the requirement to contain all the
elements of a given set
"""


def k_permutations(items, n):
    if n == 0:
        yield []
    else:
        for item in items:
            for kp in k_permutations(items, n - 1):
                if item not in kp:
                    yield [item] + kp


for kp in k_permutations("abcd", 3):
    print(kp)

# A Generator of Generators


def firstn(generator, n):
    g = generator()
    for i in range(n):
        yield next(g)


def fibonacci():
    """ A Fibonacci number generator """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(list(firstn(fibonacci, 100)))

# print(list(fibonacci()))  # This will generate an Infinite Fibonacci sequence

# Exercises

"""
Write a generator which computes the running average.
"""


def running_average():
    total = 0.0
    counter = 0
    average = None
    while True:
        term = yield average
        total += term
        counter += 1
        average = total / counter


ra = running_average()  # initialize the coroutine

next(ra)                # we have to start the coroutine

for value in [7, 13, 17, 231, 12, 8, 3]:
    out_str = "sent: {val:3d}, new average: {avg:6.2f}"
    print(out_str.format(val=value, avg=ra.send(value)))

"""
Write a generator frange, which behaves like range but accepts float values.
"""


def frange(*args):
    """  dfgdg """

    startval = 0
    stepsize = 1

    if len(args) == 1:
        endval = args[0]
    elif len(args) == 2:
        startval, endval = args
    elif len(args) == 3:
        startval, endval, stepsize = args
    else:
        txt = "range expected at most 3 arguments, got " + len(args)
        raise TypeError(txt)

    value = startval
    factor = -1 if stepsize < 0 else 1

    while (value - endval) * (factor) < 0:
        yield value
        value += stepsize

# Using frange may llok like this:


for i in frange(5.6):
    print(i, end=", ")
print()
for i in frange(0.3, 5.6):
    print(i, end=", ")
print()
for i in frange(0.3, 5.6, 0.8):
    print(i, end=", ")
print()

"""
3) Write a generator trange, which generates a sequence of time tuples from
start to stop incremented by step.
A time tuple is a 3-tuple of integers: (hours, minutes, seconds) So a call to
trange might look like this:

trange((10, 10, 10), (13, 50, 15), (0, 15, 12) )
"""


def trange(start, stop, step):
    """
    trange(stop) -> time as a 3-tuple (hours, minutes, seconds)
    trange(start, stop[, step]) -> time tuple
    start: time tuple (hours, minutes, seconds)
    stop: time tuple
    step: time tuple
    returns a sequence of time tuples from start to stop incremented by step
    """

    current = list(start)

    while current < list(stop):
        yield tuple(current)
        seconds = step[2] + current[2]
        min_borrow = 0
        hours_borrow = 0
        if seconds < 60:
            current[2] = seconds
        else:
            current[2] = seconds - 60
            min_borrow = 1
        minutes = step[1] + current[1] + min_borrow
        if minutes < 60:
            current[1] = minutes
        else:
            current[1] = minutes - 60
            hours_borrow = 1
        hours = step[0] + current[0] + hours_borrow
        if hours < 24:
            current[0] = hours
        else:
            current[0] = hours - 24


# from timerange import trange
for time in trange((10, 10, 10), (19, 53, 15), (1, 24, 12)):
    print(time)

"""
Write a version "rtrange" of the previous generator, which can receive messages
to reset the start value.
"""


def rtrange(start, stop, step):
    """
    trange(stop) -> time as a 3-tuple (hours, minutes, seconds)
    trange(start, stop[, step]) -> time tuple
    start: time tuple (hours, minutes, seconds)
    stop: time tuple
    step: time tuple
    returns a sequence of time tuples from start to stop incremented by step
    The generator can be reset by sending a new "start" value.
    """

    current = list(start)

    while current < list(stop):
        new_start = yield tuple(current)
        if new_start != None:
            current = list(new_start)
            continue
        seconds = step[2] + current[2]
        min_borrow = 0
        hours_borrow = 0
        if seconds < 60:
            current[2] = seconds
        else:
            current[2] = seconds - 60
            min_borrow = 1
        minutes = step[1] + current[1] + min_borrow
        if minutes < 60:
            current[1] = minutes
        else:
            current[1] = minutes - 60
            hours_borrow = 1
        hours = step[0] + current[0] + hours_borrow
        if hours < 24:
            current[0] = hours
        else:
            current[0] = hours - 24


# from rtimerange import rtrange
ts = rtrange((10, 10, 10), (17, 50, 15), (1, 15, 12))

for _ in range(3):
    print(next(ts))

print(ts.send((8, 5, 50)))

for _ in range(3):
    print(next(ts))

"""
Write a program, using the newly written generator "trange", to create a file
"times_and_temperatures.txt". The lines of this file contain a time in the format
hh::mm::ss and random temperatures between 10.0 and 25.0 degrees. The times
should be ascending in steps of 90 seconds starting with 6:00:00. For example:

06:00:00 20.1
06:01:30 16.1
06:03:00 16.9
06:04:30 13.4
06:06:00 23.7
06:07:30 23.6
06:09:00 17.5
06:10:30 11.0

Bitstream of zeroes and ones
P(1) = p
"""

# from timerange import trange


fh = open("times_and_temperatures.txt", "w")

for time in trange((6, 0, 0), (23, 0, 0), (0, 1, 30)):
    random_number = random.randint(100, 250) / 10
    lst = time + (random_number,)
    output = "{:02d}:{:02d}:{:02d}{:4.1f}\n".format(*lst)
    fh.write(output)

# You can find further details and the mathematical background about this
# exercise in our chapter on:
# https://python-course.eu/weighted_choice_and_sample.php

"""
Write a generator with the name "random_ones_and_zeroes", which returns a
bitstream, i.e. a zero or a one in every iteration. The probability p for
returning a 1 is defined in a variable p. The generator will initialize this
value to 0.5. In other words, zeroes and ones will be returned with the
same probability.
"""


def random_ones_and_zeros():
    p = 0.5
    while True:
        x = random.random()
        message = yield 1 if x < p else 0
        if message != None:
            p = message


x = random_ones_and_zeros()

next(x)  # we are not interested in the return value

for p in [0.2, 0.8]:
    print("\nWe change the probability to : " + str(p))
    x.send(p)
    for i in range(20):
        print(next(x), end=" ")

print()

"""
We wrote a class Cycle in the beginning of this chapter of our Python tutorial.
Write a generator cycle performing the same task.
"""


def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


countries = ["Brasil", "Argentina", "Uruguay"]

country_iterator = cycle(countries)

for i in range(7):
    print(next(country_iterator))
