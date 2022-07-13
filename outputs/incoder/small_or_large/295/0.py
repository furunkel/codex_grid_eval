
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "large" if n >= 2000 (and None if 2 <= n < 2000).
    """
    if n < 2:
        return "mouse"
    if n >= 2000:
        return "large"
    return None


# ______________________________________________________________________________
# Problem 5


def fibonacci(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# ______________________________________________________________________________
# Problem 6


def fibonacci_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using an iterative approach.
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# ______________________________________________________________________________
# Problem 7


def fibonacci_memoization(n):
    """
    Given an integer n, return the nth Fibonacci number using memoization.
    """
    memo = {}
    def fibonacci(n):
        if n not in memo:
            memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]
    return fibonacci(n)


# ______________________________________________________________________________
# Problem 8


def fibonacci_memoization_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using an iterative and memoization approach.
    """
    memo = {}
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        if i not in memo:
            memo[i] = fibonacci_iterative(i - 1) + fibonacci_iterative(i - 2)
    return memo[a]


# ______________________________________________________________________________
# Problem 9


def fibonacci_memoization_recursive(n):
    """
    Given an integer n, return the nth Fibonacci number using an iterative and memoization approach.
    """
    memo = {}
    def fibonacci(n):
        if n not in memo:
            memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return memo[n]
    return fibonacci(n)


# ______________________________________________________________________________
# Problem 10


def fibonacci_memoization_recursive_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number using an iterative and memoization approach.
    """
    memo = {}
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        if i not in memo:
            memo[i] = fibonacci_memoization_re