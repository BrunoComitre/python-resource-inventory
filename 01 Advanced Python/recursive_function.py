# https://python-course.eu/advanced-python/recursive-functions.php

'''
Recursion has something to do with infinity.

Recursion is a method of programming or coding a problem, in which a function
calls itself one or more times in its body. Usually, it is returning the return
value of this function call. If a function definition satisfies the condition
of recursion, we call this function a recursive function.

Termination condition: A recursive function has to fulfil an important
condition to be used in a program: it has to terminate. A recursive function
terminates, if with every recursive call the solution of the problem is
downsized and moves towards a base case. A base case is a case, where the
problem can be solved without further recursion. A recursion can end up in an
infinite loop, if the base case is not met in the calls.

Example:

4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1

Replacing the calculated values gives us the following expression

4! = 4 * 3 * 2 * 1
In other words, recursion in computer science is a method where the solution to
a problem is based on solving smaller instances of the same problem.

Recursive Functions in Python:

def factorial (n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
'''

# Recursive Function Factorial


from math import sqrt
from timeit import Timer


def factorial(n: int) -> int:
    print(f'Factorial has been called with n: {str(n)}')
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print(f'Intermediate result for {n} * factorial {n-1} is {res}')
        return res


print(factorial(5))

# Iterative Function Factorial


def factorial_iterative(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


for i in range(5):
    print(f'Factorial {i} = {factorial_iterative(i)}')


''''
A module containing both a recursive and an iterative implementation of the
Fibonacci Function.

The purpse of this module consists in showing the inefficiency of a purely
recursive implementation of the Fibonacci Function.
'''

# Recursive Function Fibonacci


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(5):
    print(f'Fibonacci {i} = {fibonacci(i)}')

# Iterative Function Fibonacci


def fibonacci_iterative(n: int) -> int:
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n - 1):
        old, new = new, old + new
    return new


for i in range(10):
    print(f'Fibonacci {i} = {fibonacci_iterative(i)}')


# Recursive Fibonacci function which memoizes previously calculated values with
# the help of a dictionary memo

memo = {0: 0, 1: 1}


def fibonacci_memory(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci_memory(n - 1) + fibonacci_memory(n - 2)
    return memo[n]

# Compare time of execution of recursive and iterative Fibonacci functions


t1 = Timer("fibonacci(10)", "from __main__ import fibonacci")


for i in range(1, 20):
    cmd = "fibonacci(" + str(i) + ")"
    t1 = Timer(cmd, "fibonacci")
    time1 = t1.timeit(3)
    cmd = "fibonacci_iterative(" + str(i) + ")"
    t2 = Timer(cmd, "fibonacci_iterative")
    time2 = t2.timeit(3)
    print(f'n = {i:2d},'
          'fibonacci: {time1:8.6f},'
          'fibonacci_iterative:  {time2:7.6f},'
          'time1/time2: {time1/time2:10.2f}')

# Using Recursive Fibonacci Function with callable objects


class FibonacciLike(object):

    def __init__(self, i1=0, i2=1):
        self.memo = {0: i1, 1: i2}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.memo[n]


# We create a callable to create the Fibonacci numbers:
fib = FibonacciLike()

# This will create a callable to create the Lucas number series:
lucas = FibonacciLike(2, 1)

for i in range(1, 16):
    print(i, fib(i), lucas(i))

'''
The Lucas numbers or Lucas series are an integer sequence named after the
mathematician François Édouard Anatole Lucas (1842-91), who studied both that
sequence and the closely related Fibonacci numbers. The Lucas numbers have the
same creation rule as the Fibonacci number, i.e. the sum of the two previous
numbers, but the values for 0 and 1 are different.
'''

# Recursive Fibonacci function which Generalizes to any callable object


class kFibonacci:

    def __init__(self, k, initials, coefficients):
        self.memo = dict(zip(range(k), initials))
        self.coeffs = coefficients
        self.k = k

    def __call__(self, n):
        k = self.k
        if n not in self.memo:
            result = 0
            for coeff, i in zip(self.coeffs, range(1, k + 1)):
                result += coeff * self.__call__(n - i)
            self.memo[n] = result
        return self.memo[n]


fib = kFibonacci(2, (0, 1), (1, 1))
lucas = kFibonacci(2, (2, 1), (1, 1))

for i in range(1, 16):
    print(i, fib(i), lucas(i))

# Using Pell sequence: to starts: 1, 2, 5, 12, 29, ...

P = kFibonacci(2, (1, 2), (2, 1))

for i in range(10):
    print(i, P(i))

# Using the sum of previous two Pell Numbers between two Pell Numbers:
# P(i) and P(i+1)


def nP(n):
    if n < 2:
        return P(n)
    else:
        i = n // 2 + 1
        if n % 2:  # n is odd
            return P(i)
        else:
            return P(i-1) + P(i-2)


for i in range(20):
    print(nP(i), end=", ")

nP = kFibonacci(4, (1, 2, 3, 5), (0, 2, 0, 1))
for i in range(20):
    print(nP(i), end=", ")

# Exercises

'''
Think of a recursive version of the function f(n) = 3 * n,
i.e. the multiples of 3
'''


def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3


for i in range(1, 10):
    print(mult3(i))

'''
Write a recursive Python function that returns the sum of the first n integers.
(Hint: The function will be similiar to the factorial function!)
'''


def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)


'''
Write a function which implements the Pascal's triangle:
                 1

              1    1

          1     2     1

       1     3     3     1

   1     4     6     4     1

1     5     10    10     5    1
'''


def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line


print(pascal(6))

'''
The Fibonacci numbers are hidden inside of Pascal's triangle.
If you sum up the coloured numbers of the following triangle,
you will get the 7th Fibonacci number:

                        1
                    1       1
                1       2      1
            1       3       3     1
        1       4       6      4     1
     1      5      10      10     5     1
1       6       15      20     15     6     1

Write a recursive program to calculate the Fibonacci numbers,
using Pascal's triangle.
'''


def fib_pascal(n, fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)


def fib(n):
    return fib_pascal(n, 0)[1]


for i in range(1, 10):
    print(fib(i))

'''
Implement a recursive function in Python for the sieve of Eratosthenes.

The sieve of Eratosthenes is a simple algorithm for finding all prime numbers
up to a specified integer. It was created by the ancient Greek mathematician
Eratosthenes. The algorithm to find all the prime numbers less than or equal to
a given integer n:

1. Create a list of integers from two to n: 2, 3, 4, ..., n
2. Start with a counter i set to 2, i.e. the first prime number
3. Starting from i+i, count up by i and remove those numbers from the list,
   i.e. 2i, 3i, 4*i, etc..
4. Find the first number of the list following i. This is the next prime number
5. Set i to the number found in the previous step
6. Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's
   enough to go to the square root of n)
7. All the numbers, which are still in the list, are prime numbers

You can easily see that we would be inefficient, if we strictly used this
algorithm, e.g. we will try to remove the multiples of 4, although they have
been already removed by the multiples of 2. So it's enough to produce the
multiples of all the prime numbers up to the square root of n. We can
recursively create these sets.
'''


def sieve(n):
    # returns all primes between 2 and n
    primes = list(range(2, n+1))
    max = sqrt(n)
    num = 2
    while num < max:
        i = num
        while i <= n:
            i += num
            if i in primes:
                primes.remove(i)
        for j in primes:
            if j > num:
                num = j
                break
    return primes


print(sieve(100))

'''
Write a recursive function fib_indexfib(), which returns the index of a number
in the Fibonacci sequence, if the number is an element of this sequence, and
returns -1 if the number is not contained in it, i.e.
'''


def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


print(primes(100))

'''
The sum of the squares of two consecutive Fibonacci numbers is also a Fibonacci
number, e.g. 2 and 3 are elements of the Fibonacci sequence and 22 + 33 = 13
corresponds to Fib(7).Use the previous function to find the position of the sum
of the squares of two consecutive numbers in the Fibonacci sequence.

Mathematical explanation: Let a and b be two successive Fibonacci numbers with
a prior to b. Fibonacci sequence starting with the number "a" looks like this:

0   a
1   b
2   a + b
3   a + 2b
4   2a + 3b
5   3a + 5b
6   5a + 8b

We can see that the Fibonacci numbers appear as factors for a and b. The n-th
element in this sequence can be calculated with the following formula.

From this we can conclude that for a natural number n, n>1, the following
holds true
'''

memo = {0: 0, 1: 1}


def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


def fib_index(*x):
    """ finds the natural number i with fib(i) == n """
    if len(x) == 1:
        # started by user and find index starting from 0
        return fib_index(x[0], 0)
    else:
        n = fib(x[1])
        m = x[0]
        if n > m:
            return -1
        elif n == m:
            return x[1]
        else:
            return fib_index(m, x[1]+1)


# code from the previous example with the functions fib() and find_index()

print(" index of a |    a |     b | sum of squares | index ")
print("=====================================================")
for i in range(15):
    sqr = fib(i)**2 + fib(i+1)**2
    print(f"{i:12d}|{fib(i):6d}|{fib(i+1):9d}|{sqr:14d}|{fib_index(sqr):5d}")

'''
The tribonacci numbers are like the Fibonacci numbers, but instead of starting
with two predetermined terms, the sequence starts with three predetermined
terms and each term afterwards is the sum of the preceding three terms. The
first few tribonacci numbers are:

0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768,
10609, 19513, 35890, 66012, ...

The tetranacci numbers start with four predetermined terms, each term
afterwards being the sum of the preceding four terms. The first few tetranacci
numbers are:

0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773, 1490, 2872, 5536,
10671, 20569, 39648, ...

This continues in the same way for pentanacci, hexanacci, heptanacci,
octanacci, and so on.

Write a function for the tribonacci and tetranacci numbers.
'''

tribonacci = kFibonacci(3, (0, 0, 1), (1, 1, 1))

for i in range(20):
    print(tribonacci(i), end=", ")

tetranacci = kFibonacci(4, (0, 0, 0, 1), (1, 1, 1, 1))

for i in range(20):
    print(tetranacci(i), end=", ")

octanacci = kFibonacci(8, (0, 0, 0, 0, 0, 0, 0, 1), (1, 1, 1, 1, 1, 1, 1, 1))

for i in range(20):
    print(octanacci(i), end=", ")

prefixes = ['tribo', 'tetra', 'pentra', 'hexa', 'hepta', 'octa']
for k, prefix in zip(range(len(prefixes)), prefixes):
    cmd = prefix + "nacci = kFibonacci("
    cmd += str(k+3) + ", (" + "0, " * (k+2) + "1), "
    cmd += "(" + "1, " * (k+2) + "1))"
    print(cmd)
    exec(cmd)

print("\nTesting the octanacci function: ")
for i in range(20):
    print(octanacci(i), end=", ")

'''
What if somebody wants to check the parameters in a recursive function?
For example the factorial function. Okay, please write a recursive version of
factorial, which checks the parameters. Maybe you did it in a perfect way, but
maybe not. Can you improve your version? Get rid of unnecessary tests?
'''

# Calculates the factorial of n, n should be an integer and n <= 0


def factorial(n):
    def inner_factorial(n):
        if n == 0:
            return 1
        else:
            return n * inner_factorial(n-1)
    if type(n) == int and n >= 0:
        return inner_factorial(n)
    else:
        raise TypeError("n should be a positve int or 0")


print(factorial(10))
