
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "small" if n >= 15 (and neither if 2 <= n < 15).
    """
    if n < 2:
        return "mouse"
    elif n >= 15:
        return "small"
    else:
        return "large"

# ______________________________________________________________________________
# Problem 5
# ______________________________________________________________________________
def fibonacci(n):
    """
        Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, ...
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
        Iterative implementation of fibonacci
    """
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

# ______________________________________________________________________________
# Problem 7
# ______________________________________________________________________________
def primes_sieve(limit):
    """
        Implementation of Sieve of Eratosthenes algorithm
    """
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, limit):
        if numbers[i]:
            for j in range(i * i, limit, i):
                numbers[j] = False

    return [i for i in range(2, limit) if numbers[i]]

# ______________________________________________________________________________
# Problem 8
# ______________________________________________________________________________
def primes_sieve_iterative(limit):
    """
        Iterative implementation of Sieve of Eratosthenes
    """
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, limit):
        if numbers[i]:
            for j in range(i * i, limit, i):
                numbers[j] = False

    primes = []
    for i in range(2, limit):
        if numbers[i]:
            primes.append(i)

    return primes

# ______________________________________________________________________________
# Problem 9
# ______________________________________________________________________________
def primes_sieve_python(limit):
    """
        Python implementation of Sieve of Eratosthenes
    """
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False

    for i in range(2, limit):
        if numbers[i]:
            for j in range(i * i, limit, i):
                numbers[j] = False

    primes = []
    for i in range(2, limit):
        if numbers[i]:
            primes.append(i)

    return primes

# ______________________________________________________________________________
# Problem 10
# ______________________________________________________________________________
def primes_sieve2(limit):
    """
        Implementation of Sieve of Eratosthenes algorithm
    """
    number