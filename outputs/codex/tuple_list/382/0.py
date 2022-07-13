
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(lst, key=lambda x: x[1])[0]


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


def fibonacci_generator(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci_generator_2(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci_generator_3(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fibonacci_generator_4(n):
    """
    Given a number n, write a function that returns the nth number in the Fibonacci sequence.
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a,