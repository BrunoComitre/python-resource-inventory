# TUTORIAL DE : https://realpython.com/python-kwargs-and-args/

def my_sum(a: int, b: int) -> int:
    return a + b

print(my_sum(1, 2))


a = [*"PythonProgramming"]
print(a)

*a, = "PythonProgramming"
print(a)
