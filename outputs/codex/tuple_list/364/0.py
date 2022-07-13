
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(lst, key=lambda x: x[0])[1]


def fibonacci_recursive(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


def fibonacci_memoized(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            cache[n] = fib(n - 1) + fib(n - 2)
            return cache[n]

    return fib(n)


def fibonacci_memoized_2(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            cache[n] = fib(n - 1) + fib(n - 2)
            return cache[n]

    return fib(n)


def fibonacci_memoized_3(n):
    """
    Given a number n, write a function that returns the nth number in