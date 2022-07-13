
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 1000 and "small" if n >= 2000 (and neither if 1000 <= n < 2000).
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
    Given an integer n, return the nth Fibonacci number calculated iteratively.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b

# ______________________________________________________________________________
# Problem 7

def primes(n):
    """
    Return a list of the first n primes.
    """
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3, 3]
    else:
        sieve = range(3, n + 1, 2) # exclude 2 and all multiples of 3
        sieve.extend([True] * (n - len(sieve)))
        for i in sieve:
            if i:
                sieve[i*i::2*i] = [False] * ((n - i*i - 1) // (2 * i) + 1)
        return [2] + [2*i + 1 for i in xrange(3, n) if i not in sieve]

# ______________________________________________________________________________
# Problem 8

def primes_sieve(n):
    """
    Return a list of the first n primes, using Sieve of Eratosthenes.
    """
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3, 3]
    else:
        sieve = range(3, n + 1, 2) # exclude 2 and all multiples of 3
        sieve.extend([True] * (n - len(sieve)))
        for i in sieve:
            if i:
                sieve[i*i::2*i] = [False] * ((n - i*i - 1) // (2 * i) + 1)
        return [2] + [2*i + 1 for i in xrange(3, n) if i not in sieve]

# ______________________________________________________________________________
# Problem 9

def fibonacci_memoization(n):
    """
    Given an integer n, return the nth Fibonacci number calculated iteratively using a dictionary of previously calculated values
    """
    if n < 2:
        return n
    else:
        if n in fibonacci_memoization.keys():
            return fibonacci_memoization[n]
        else:
            fibonacci_memoization[n] = fibonacci