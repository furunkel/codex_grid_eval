
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "large" if n >= 15 (and None if 2 <= n < 15).
    """
    if n < 2:
        return "mouse"
    if n >= 15:
        return "large"
    return None


# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n < 2:
        return n
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
    Return the nth number in the Fibonacci sequence using memoization
    """
    memo = {}
    def fib(n):
        if n < 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)


# ______________________________________________________________________________
# Problem 8

def fibonacci_memoization_iterative(n):
    """
    Return the nth number in the Fibonacci sequence using memoization
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b in memo:
            return memo[b]
        memo[b] = b
    return b


# ______________________________________________________________________________
# Problem 9

def primes_sieve(limit):
    """
    Return a list containing the first n prime numbers.
    
    Usage: primes_sieve(100)
    """
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for p in range(3, int(limit ** 0.5) + 1, 2):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return [p for p in range(3, limit) if sieve[p]]


# ______________________________________________________________________________
# Problem 10

def primes_sieve_iterative(limit):
    """
    Return a list containing the first n prime numbers.
    
    Usage: primes_sieve_iterative(100)
    """
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for p in range(3, int(limit ** 0.5) + 1, 2):
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return sieve


# 