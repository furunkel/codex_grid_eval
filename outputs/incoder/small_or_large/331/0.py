
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and neither if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
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
    Given an integer n, return the nth Fibonacci number using an iterative approach.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 7

def primes(n):
    """
    Return a list of the first n prime numbers.
    """
    if n < 2:
        return []
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False
    return [p for p in range(2, n) if sieve[p]]

# ______________________________________________________________________________
# Problem 8

def primes_iterative(n):
    """
    Return a list of the first n prime numbers using an iterative approach.
    """
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    p = 3
    while sieve[p]:
        for i in range(p * p, n, p):
            sieve[i] = False
        p += 1
    return [2] + [p + 1 for p in range(3, n, 2) if sieve[p]]

# ______________________________________________________________________________
# Problem 9

def power_iterative(x, n):
    """
    Given a number x and an integer n, return the nth power of the number x.
    """
    result = 1
    for i in range(n):
        result *= x
    return result

# ______________________________________________________________________________
# Problem 10

def power_set(n):
    """
    Return a set of all the powers of 2 up to the number n.
    """
    return {p for p in range(1, n + 1)}

# ______________________________________________________________________________
# Problem 11

def prime_factors(n):
    """
    Return a list of the prime factors of n.
    """
    if n < 2:
        return []
    factors = []
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors

