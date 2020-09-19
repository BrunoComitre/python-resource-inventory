# TUTORIAL DE : https://realpython.com/python-kwargs-and-args/

def my_sum(*args: tuple) -> int:
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))

# Observe que argsé apenas um nome. Você não é obrigado a usar o nome args.
# Você pode escolher qualquer nome de sua preferência, como integers:
def my_sum_integers(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum_integers(1, 2, 3, 4, 5, 6, 7, 8, 9))

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))
