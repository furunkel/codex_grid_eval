
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < 0:
        return "mouse"
    elif n >= 2:
        return "house"
    else:
        return None


# ______________________________________________________________________________
# Problem 5


def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
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


def fibonacci_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    mem = {}
    if n not in mem:
        mem[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return mem[n]


# ______________________________________________________________________________
# Problem 8


def fibonacci_memoization(max_n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    mem = {}
    mem[0] = 0
    mem[1] = 1
    for i in range(2, max_n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]
    return mem[max_n]


# ______________________________________________________________________________
# Problem 9


def fibonacci_bottom_up(max_n):
    """
    Return the nth number in the Fibonacci sequence using bottom up dynamic programming
    """
    mem = {}
    mem[0] = 0
    mem[1] = 1
    for i in range(2, max_n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]
    return mem[max_n]


# ______________________________________________________________________________
# Problem 10


def fibonacci_bottom_up_iterative(n):
    """
    Return the nth number in the Fibonacci sequence using bottom up dynamic programming
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


# ______________________________________________________________________________
# Problem 11


def fibonacci_bottom_up_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using bottom up dynamic programming
    """
    mem = {}
    mem[0] = 0
    mem[1] = 1
    for i in range(