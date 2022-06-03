# https://paulgray.net/the-state-monad/

# Imperative programming
import math
from random import randint


def random_number_generator(seed: int) -> int:
    nextSeed = (1839567234 * seed + 972348567) % 8239451023
    return nextSeed


seed = 1
randomNumber1 = random_number_generator(seed)
randomNumber2 = random_number_generator(randomNumber1)

print(randomNumber1)
print(randomNumber2)

# Generate random with interval


def random_in_range_equal(seed: int, minium: int, maximum: int) -> int:
    nextSeed = random_number_generator(seed)
    random = minium + math.floor((nextSeed / maximum) * (maximum - minium))
    return random


seed = 1
random1 = random_in_range_equal(seed, 0, 10)
random2 = random_in_range_equal(seed, 0, 10)

print(random1)
print(random2)


def random_in_range(seed: int, minium: int, maximum: int) -> list[int]:
    nextSeed = random_number_generator(seed)
    random = minium + math.floor((nextSeed / maximum) * (maximum - minium))
    return [nextSeed, random]


seed1 = 1
[seed2, random1] = random_in_range(seed1, 0, 10)
[seed3, random2] = random_in_range(seed2, 0, 10)

print([seed2, random1])
print([seed3, random2])

FirstNames = ['João', 'Maria', 'José', 'Carla']


def random_first_name(seed: int):
    [seed2, ranged] = random_in_range(seed, 0, len(FirstNames))
    return [seed2, FirstNames[ranged]]
