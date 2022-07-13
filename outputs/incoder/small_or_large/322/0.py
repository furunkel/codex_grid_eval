
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= 15 (and neither if -100 <= n < 15).
    """
    if n < 0:
        return "mouse"
    elif n >= 15:
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
        return fibonacci(n - 2) + fibonacci(n - 1)

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
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i) // i)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]

# ______________________________________________________________________________
# Problem 8

def primes_iter(n):
    """
    Return a list of the first n prime numbers using an iterative approach.
    """
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i) // i)
            yield i

# ______________________________________________________________________________
# Problem 9

def power_iter(x, n):
    """
    Return an iterator that computes x ** n for n >= 0.
    """
    if n == 0:
        yield 1
    else:
        for i in power_iter(x , n - 1):
            yield i * x

# ______________________________________________________________________________
# Problem 10

def fibonacci_memoize(f):
    """
    Decorator that caches the results of function calls with different arguments.
    """
    memory = {}
    
    def helper(x):
        if x not in memory:
            memory[x] = f(x)
        return memory[x]
    
    return helper

@fibonacci_memoize
def fibonacci_recursive(n):
    """
    Using a recursive implementation, find the nth Fibonacci number.
    """
    if n < 2:
        return n
    else:
        return 