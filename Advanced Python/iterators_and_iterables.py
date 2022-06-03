# https://python-course.eu/advanced-python/iterable-iterator.php

'''
You can iterate with a for loop over iterators and iterables.
Every iterator is also an iterable, but not every iterable is an iterator.

So if you want to add an iterator behavior to your class,
you have to add the __iter__ and the __next__ method to your class.
'''

# Iterating over a list and string

for city in ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]:
    print(city)

for programming_language in ["Python", "TypeScript", "C++"]:
    print(programming_language)

for char in "Iteration is easy":
    print(char)

cities = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
iterator_object = iter(cities)

print(iterator_object)
print(next(iterator_object))
print(next(iterator_object))
print(next(iterator_object))

# Return StopIteration if there are no more elements
# print(next(iterator_object))


def iterable(object: object) -> bool:
    try:
        iter(object)
        return True
    except TypeError:
        return False


for element in [34, [4, 5], (4, 5), {"a": 4}, "dfsdf", 4.5]:
    print(f'{element} is iterable: {iterable(element)}')

# Creating a class for iterators for looping over a sequence backards


class Reverse:
    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data)

    def __iter__(self) -> object:
        return self

    def __next__(self) -> object:
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


list_of_numbers = [12, 345, 6789]
list_of_numbers_reversed = Reverse(list_of_numbers)

for element in list_of_numbers_reversed:
    print(element)
