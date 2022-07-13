
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= 15 (and neither if -100 <= n < 15).
    """
    if n < -100:
        return "small"
    elif n >= 15:
        return "house"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# ______________________________________________________________________________
# Problem 6

def fibonacci_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using an iterative approach.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 7

def fibonacci_memoization(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    memo = {}
    def fib(n):
        if n not in memo:
            memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)

# ______________________________________________________________________________
# Problem 8

def fibonacci_memoization_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
    return memo[b]

# ______________________________________________________________________________
# Problem 9

def fibonacci_memoization_recursive(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    if n < 2:
        return n
    else:
        return fibonacci_memoization_recursive(n - 1) + fibonacci_memoization_recursive(n - 2)

# ______________________________________________________________________________
# Problem 10

def fibonacci_memoization_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
    return memo[b]

# ______________________________________________________________________________
# Problem 11

def fibonacci_memoization_recursive(n):
    """
    Given an integer n, return the nth Fibonacci number using a recursive approach.
    """
    if n < 2:
