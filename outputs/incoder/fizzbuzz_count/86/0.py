
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz(3298)
    204
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative(3298)
    204
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_memoized(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_memoized(3298)
    204
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_memoized(3298)
    204
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_memoized_iterative(3298)
    204
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized_iterative_memoized(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_memoized_iterative_memoized(3298)
    204
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_memoized_iterative_memoized_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_bu