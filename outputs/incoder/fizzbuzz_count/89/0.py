
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    98
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative(3298)
    98
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast(3298)
    98
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fast2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast2(3298)
    98
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fast3(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast3(3298)
    98
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fast4(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast4(3298)
    98
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fast5(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fi