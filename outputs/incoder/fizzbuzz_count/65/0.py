
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(3298)
    73
    """
    count = 0
    while n > 0:
        if n % 1837 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative(3298)
    73
    """
    count = 0
    while n > 0:
        if n % 1837 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_memoized(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_memoized(3298)
    73
    """
    count = 0
    while n > 0:
        if n % 1837 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_memoized(3298)
    73
    """
    count = 0
    while n > 0:
        if n % 1837 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_memoized_iterative(3298)
    73
    """
    count = 0
    while n > 0:
        if n % 1837 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized_iterative_memoized(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_memoized_iterative_memoized(3298)
    73
    """
    count = 0
    while n > 0:
        if n % 1837 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized_iterative_memoized_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_memoized_iterative_memoized_iterative(32