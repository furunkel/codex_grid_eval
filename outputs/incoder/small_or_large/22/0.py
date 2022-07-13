
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "large" if n >= 15 (and None if 2 <= n < 15).
    """
    if n < 2:
        return "small"
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


def fibonacci_memoization(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    memo = {}
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]


# ______________________________________________________________________________
# Problem 8
# ______________________________________________________________________________


def fibonacci_memoization_iterative(n):
    """
    Return the nth number in the Fibonacci sequence using dynamic programming
    """
    memo = {}
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
        if b not in memo:
            memo[b] = a
    return memo[b]


# ______________________________________________________________________________
# Problem 9
# ______________________________________________________________________________


def prime_factors_iterative(n):
    """
    Return a list of the first n prime factors
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# ______________________________________________________________________________
# Problem 10
# ______________________________________________________________________________


def prime_factors_memoization(n):
    """
    Return a list of the first n prime factors
    """
    factors = []
    memo = {}
    if n in memo:
        return memo[n]
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
