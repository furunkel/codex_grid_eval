
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "small"
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
        return fibonacci(n - 2) + fibonacci(n - 1)


# ______________________________________________________________________________
# Problem 6

def fibonacci_iterative(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a


# ______________________________________________________________________________
# Problem 7

def primes(n):
    """
    Given an integer n, return a list of all the prime numbers less than or equal to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for p in range(2, n + 1):
        if sieve[p]:
            for i in range(p * 2, n + 1, p):
                sieve[i] = False

    return [p for p in range(n + 1) if sieve[p]]


# ______________________________________________________________________________
# Problem 8

def primes_iterative(n):
    """
    Given an integer n, return a list of all the prime numbers less than or equal to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for p in range(2, n + 1):
        if sieve[p]:
            for i in range(p * 2, n + 1, p):
                sieve[i] = False

    return [2] + [p for p in range(n + 1) if sieve[p]]


# ______________________________________________________________________________
# Problem 9

def power_iterative(x, n):
    """
    Given a number x and an integer n, return the nth power of x to the nth power.
    """
    result = 1
    for i in range(n):
        result *= x
    return result


# ______________________________________________________________________________
# Problem 10

def fibonacci_memoization(n):
    """
    Given an integer n, return the nth Fibonacci number.
    """
    if n < 2:
        return n
    else:
        return fibonacci_memoization(n - 2) + fibonacci_memoization(n - 1)


# ______________________________________________________________________________
# Problem 11

def fibonacci_memoization(n_list):
    """
    Given a list of integers n_list, return the nth Fibonacci number for each element in the list.
    """
    n_list = n_list[::-1]
    n_list[0] = 0
    n_list[1] = 1
