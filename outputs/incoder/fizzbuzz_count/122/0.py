
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz(3298)
    331
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
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative(3298)
    331
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_fast(3298)
    331
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fastest(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_fastest(3298)
    331
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_faster(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_faster(3298)
    331
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fastester(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_fastester(3298)
    331
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_fastester_faster(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buz