
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 1000 and "large" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "small"
    elif n >= 2000:
        return "large"
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
    Given an integer n, return the nth Fibonacci number.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b

# ______________________________________________________________________________
# Problem 7

def fibonacci_memoization(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    memo = {}
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n)
        return memo[n]

# ______________________________________________________________________________
# Problem 8

def fibonacci_memoization_with_fibonacci_cache(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    memo = {}
    def fibonacci(n):
        if n < 2:
            return n
        else:
            if n in memo:
                return memo[n]
            else:
                memo[n] = fibonacci_with_fibonacci_cache(n - 1) + fibonacci_with_fibonacci_cache(n - 2)
                return memo[n]
    def fibonacci_with_fibonacci_cache(n):
        if n < 2:
            return n
        else:
            a, b = 0, 1
            while b < n:
                a, b = b, a + b
            return b
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n)
        return memo[n]

# ______________________________________________________________________________
# Problem 9

def fibonacci_memoization_with_fibonacci_cache_and_fibonacci_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    memo = {}
    def fibonacci(n):
        if n < 2:
            return n
        else:
            if n in memo:
                return memo[n]
            else:
                memo[n] = fibonacci_