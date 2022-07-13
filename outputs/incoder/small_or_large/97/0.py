
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < 0:
        return "small"
    elif n >= 2:
        return "house"
    else:
        return None


# ______________________________________________________________________________
# Problem 5


def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ______________________________________________________________________________
# Problem 6


def fibonacci_iterative(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


# ______________________________________________________________________________
# Problem 7


def power_iterative(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a ** b
    return a


# ______________________________________________________________________________
# Problem 8


def fibonacci_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using a
    cache to save previously computed values
    """
    cache = {0: 0, 1: 1}
    if n in cache:
        return cache[n]
    while len(cache) < n:
        a, b = b, a + b
        cache[b] = a
    return cache[n]


# ______________________________________________________________________________
# Problem 9


def fibonacci_memoization(squares):
    """
    Return the nth number in the Fibonacci sequence using a
    cache to save previously computed values
    """
    cache = {0: 0, 1: 1}
    if squares[0] in cache:
        return cache[squares[0]]
    while len(cache) < len(squares):
        a, b = b, a + b
        cache[b] = a
    return cache[len(squares)]


# ______________________________________________________________________________
# Problem 10


def fibonacci_memoization(squares):
    """
    Return the nth number in the Fibonacci sequence using a
    cache to save previously computed values
    """
    cache = {0: 0, 1: 1}
    if squares[0] in cache:
        return cache[squares[0]]
    while len(cache) < len(squares):
        a, b = b, a + b
        cache[b] = a
    return cache[len(squares)]


# ______________________________________________________________________________
# Problem 11


def fibonacci_memoization(squares):
    """
    Return the nth 