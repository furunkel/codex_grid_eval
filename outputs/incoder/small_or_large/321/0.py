
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= 2 (and neither if -100 <= n < 2).
    """
    if n < -100:
        return "mouse"
    elif n >= 2:
        return "large"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5

def f(n):
    """
        The Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    return 1 if n < 2 else f(n-1) + f(n-2)

def fib(n):
    """
        The nth Fibonacci number, where Fibonacci numbers are sequential.
    """
    return f(n)

def fib_iter(n):
    """
        Generate an infinite sequence of Fibonacci numbers, starting with value 1.
    """
    a, b = 1, 0
    while 1:
        yield a
        a, b = b, a + b

def fib_oneliner(n):
    """
        Generate the nth Fibonacci number using a one-liner.
    """
    return next(fib_iter(n))

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

def fib_series(n):
    """
        Generate a Fibonacci series up to n.
    """
    a, 