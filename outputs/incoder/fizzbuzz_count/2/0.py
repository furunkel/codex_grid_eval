
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative_fast(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative_fastest(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest_2(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative_fastest_2(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest_3(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative_fastest_3(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fastest_4(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 