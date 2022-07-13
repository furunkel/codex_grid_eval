
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(78)
    2
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        if n % 1837 == 0:
            count += 1
        n //= 1837
    return count


def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative(78)
    2
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        if n % 1837 == 0:
            count += 1
        n //= 1837
    return count


def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fast(78)
    2
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        if n % 1837 == 0:
            count += 1
        n //= 1837
    return count


def fizz_buzz_iterative_slow(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_slow(78)
    2
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        if n % 1837 == 0:
            count += 1
        n //= 1837
    return count


def fizz_buzz_iterative_fastest(n : int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fastest(78)
    2
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        if n % 1837 == 0:
            count += 1
        n //= 1837
    return count


def fizz_buzz_iterative_fastest2(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fastest2(78)
    2
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        if n % 1837 == 0:
            count += 1
        n //= 1837
    return count


def fizz_buzz_iterative_fastest3(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fastest3(78)
    2
