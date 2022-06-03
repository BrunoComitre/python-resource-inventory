# https://python-course.eu/advanced-python/currying-in-python.php

''''
Currying is the technique of decomposing the evaluation of a function that
takes multiple arguments to evaluate a sequence of single argument functions

Currying is also used in theoretical computer science, because it is often
easier to transform multiple argument models into single argument models

Mathematics:
h(x) = g(f(x))

Function:
def compor(g, f):
    def h(x):
        return g(f(x))
    return h
'''

# Real Use Case 1:


def compose(g, f):
    def h(x):
        return g(f(x))
    return h


def celsius_to_fahernheit(t: float) -> float:
    return 1.8 * t + 32


print(celsius_to_fahernheit(10))


def reajust(t: float) -> float:
    return 0.9 * t - 0.5


print(reajust(10))

convert = compose(reajust, celsius_to_fahernheit)
print(convert(10), celsius_to_fahernheit(10))

convert2 = compose(celsius_to_fahernheit, reajust)
print(convert2(10), celsius_to_fahernheit(10))

# Real Use Case 2:


def compose2(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h


def Bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


def evaluate_BMI(bmi: float) -> str:
    if bmi < 15:
        return "Very severely underweight"
    elif bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal (healthy weight)"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I (Moderately obese)"
    elif bmi < 40:
        return "Obese Class II (Severely obese)"
    else:
        return "Obese Class III (Very severely obese)"


f = compose2(evaluate_BMI, Bmi)
again = "y"

while again == "y":
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    print(f(weight, height))
    again = input("Do you want to continue? (y/n) ")

# Real Use Case 3:


def arimean(*args: float) -> float:
    return sum(args) / len(args)


def curry(f):
    # To keep the name of the curried function:
    curry.__curried_func_name__ = f.__name__
    f_args, f_kwargs = [], {}

    def f_curried(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            print(
                f'Calling curried function with: args:{args}, kwargs:{kwargs}')
            f_args += args
            f_kwargs.update(kwargs)
            print(f'Currying the values: f_args:{f_args}, f_kwargs:{f_kwargs}')
            return f_curried
        else:
            print(f'Calling {curry.__curried_func_name__} with:'
                  'f_args: {f_args}, f_kwargs: {f_kwargs}'
                  )
            result = f(*f_args, *f_kwargs)
            f_args, f_kwargs = [], {}
            return result
    return f_curried


curried_arimean = curry(arimean)
curried_arimean(2)(5)(9)(4, 5)

# It will keep on currying:
curried_arimean(5, 9)
print(curried_arimean())

# Calculating the arithmetic mean of 3, 4, and 7:
print(curried_arimean(3)(4)(7)())

# Calculating the arithmetic mean of 4, 3, and 7:
print(curried_arimean(4)(3, 7)())

# Compare it with the result of the original arimean function:
print(arimean(2, 5, 9, 4, 5, 5, 9))
print(arimean(3, 4, 7))
print(arimean(4, 3, 7))
