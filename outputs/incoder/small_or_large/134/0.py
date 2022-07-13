
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "house" if n >= 15 (and neither if 2 <= n < 15).
    """
    if n < 2:
        return "small"
    elif n >= 15:
        return "house"
    else:
        return "large"

# ______________________________________________________________________________
# Problem 5

def fibonacci(n):
    """
    Return the nth number in the Fibonacci sequence.
    """
    if n < 2:
        return n
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

def primes_sieve(limit):
    """
    Return a list containing the first n primes using the Sieve of Eratosthenes.
    """
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in xrange(3,int(limit**0.5) + 1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((limit-i*i)/(2*i)+1)
    return [2] + [i for i in xrange(3,limit,2) if sieve[i]]

# ______________________________________________________________________________
# Problem 8

def fibonacci_memoization(n):
    """
    Using a cache to save expensive function calls.
    """
    cache = {}
    def fibonacci(n):
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci(n)

# ______________________________________________________________________________
# Problem 9

def fibonacci_dynamic(n):
    """
    Dynamic Programming based implementation of the fibonacci function.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b

# ______________________________________________________________________________
# Problem 10

def fibonacci_bottom_up(n):
    """
    Bottom-up dynamic programming implementation of fibonacci.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 11

def fibonacci_bottom_up_iterative(n):
    """
    Bottom-up dynamic programming implementation of fibonacci.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return 