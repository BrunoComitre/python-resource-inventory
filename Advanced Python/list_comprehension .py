# #https://realpython.com/lessons/writing-your-first-list-comprehension/
# #https://dbader.org/blog/list-dict-set-comprehensions-in-python
# https://realpython.com/list-comprehension-python/
# https://realpython.com/courses/understand-list-comprehensions/
# https://realpython.com/courses/using-list-comprehensions-effectively/
# https://realpython.com/lessons/understand-list-comp-overview/

# List Comprehension
squares_c = [number * number for number in range(10)]
print(squares_c)

# For Loops
squares_l = []
for number in range(10):
    squares_l.append(number * number)
print(squares_l)

# List Comprehension Filter
even_squares_c = [number * number for number in range(10) if number % 2 == 0]
print(even_squares_c)

# For Loops Filter
even_squares_l = []
for number in range(10):
    if number % 2 == 0:
        even_squares_l.append(number * number)
print(even_squares_l)

"""
[List Comprehension]
    (values) = [ (expression) for (item) in (collection)]

[For Loops]
    (values) = []
    for (item) in (collection):
        (values).append( (expression) )

[List Comprehension Filter]
    (values) = [ (expression) for (item) in (collection) if (condition)]

[For Loops Filter]
    (values) = []
    for (item) in (collection):
        if (condition):
            (values).append( (expression) )
"""
