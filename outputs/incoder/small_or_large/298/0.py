
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "mouse"
    elif n >= 15:
        return "large"
    else:
        return None


# ______________________________________________________________________________
# Problem 5
# ______________________________________________________________________________


def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ______________________________________________________________________________
# Problem 6
# ______________________________________________________________________________


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
# ______________________________________________________________________________


def prime_factors(n):
    """
    Return a list of the prime factors of n
    """
    factors = []
    for p in range(2, n):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors


# ______________________________________________________________________________
# Problem 8
# ______________________________________________________________________________


def prime_factors_iterative(n):
    """
    Return a list of the prime factors of n
    """
    factors = []
    primes = []
    for p in range(2, n):
        while n % p == 0:
            factors.append(p)
            n //= p
            primes.append(p)
    if n > 1:
        factors.append(n)
        primes.append(n)
    return factors, primes


# ______________________________________________________________________________
# Problem 9
# ______________________________________________________________________________


def primes_sieve(limit):
    """
    Return a list containing the first n primes using the Sieve of Eratosthenes
    """
    sieve = [True] * limit
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * 2, limit, p):
                sieve[i] = False
        p += 1
    return [i for i, flag in enumerate(sieve) if flag]


# ______________________________________________________________________________
# Problem 10
# ______________________________________________________________________________


def primes_sieve_iterative(limit):
    """
    Return a list containing the first n primes using the Sieve of Eratosthenes
    """
    sieve = [True] * limit
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * 2, limit, p):
                sie