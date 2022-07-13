
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "house" if n >= 2000 (and None if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n >= 2000:
        return "house"
    else:
        return None


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
    Given a positive integer n, return the nth Fibonacci number.
    
    You may assume that n will always be positive.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


# ______________________________________________________________________________
# Problem 7


def primes_sieve(limit):
    """
    Return a list containing the first n prime numbers.
    
    Usage: primes_sieve(10)
    """
    sieve = [True] * (limit + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, limit + 1):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return [2] + [i for i in range(3, limit, 2) if sieve[i]]


# ______________________________________________________________________________
# Problem 8


def fibonacci_memoization(n):
    """
    Given a positive integer n, return the nth Fibonacci number.
    
    Uses a memoization to compute the Fibonacci sequence more efficiently.
    """
    memo = {}
    if n in memo:
        return memo[n]
    elif n < 2:
        return n
    else:
        memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
        return memo[n]


# ______________________________________________________________________________
# Problem 9


def fibonacci_dynamic(n):
    """
    Given a positive integer n, return the nth Fibonacci number.
    
    Uses a dynamic programming algorithm to compute the Fibonacci sequence.
    """
    if n < 2:
        return n
    else:
        return fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)


# ______________________________________________________________________________
# Problem 10


def fibonacci_bottom_up(n):
    """
    Given a positive integer n, return the nth Fibonacci number.
    
    Uses the bottom-up approach to compute the Fibonacci sequence.
    """
