
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz(50)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative(50)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fast(50)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fastest(50)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest_fast(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fastest_fast(50)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest_fastest(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fastest_fastest(50)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest_fastest_fast(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fastest_fastest_fast(50)
    3
    """
    count = 0
    while n > 0: