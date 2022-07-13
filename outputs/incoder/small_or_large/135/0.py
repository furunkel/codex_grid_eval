
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "house" if n >= 2000 (and neither if 2 <= n < 2000).
    """
    if n < 2:
        return "small"
    elif n >= 2000:
        return "house"
    else:
        return "large"

# ______________________________________________________________________________
# Problem 5

def f(n):
    """
        The function takes an integer n and returns the number of prime numbers less than or equal to n.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        count = 0
        for i in range(3, n+1, 2):
            if isprime(i):
                count += 1
        return count

# ______________________________________________________________________________
# Problem 6

def f(n):
    """
        The function takes an integer n and returns the number of prime numbers less than or equal to n.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        count = 0
        for i in range(3, n+1, 2):
            if isprime(i):
                count += 1
        return count

def isprime(n):
    """
        Determine if an integer is a prime number. Recall that 1 is not considered a prime. 
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 6
    return True

# ______________________________________________________________________________
# Problem 7

def f(n):
    """
        The function takes an integer n and returns the number of prime numbers less than or equal to n.
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        count = 0
        for i in range(3, n+1, 2):
            if isprime(i):
                count += 1
        return count

def isprime(n):
    """
        Determine if an integer is a prime number. Recall that 1 is not considered a prime. 
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 6
    return True

def primes_less_than(n):
    """
        Generate a list of prime numbers less than or equal to n
    """
    if n < 2:
        return
    elif n == 2:
        yield 2
        return
    else:
        for p in primes_less_than(n - 1):
            yield p
            yield p + 1

def primes_less_than(n):
    """
        Generate a list of prime numbers less than or equal to n
    """
    if n < 2:
        return
    elif n == 2:
        yield 2
        return
    else:
        for p in primes_less_than(n - 1):
            yield p
            yield p + 1

def primes_less_than(n):
    """
        Generate a list of prime numbers less than or equal to n
    """
    if n < 2:
        return
    elif n == 2:
        yield 2
        return