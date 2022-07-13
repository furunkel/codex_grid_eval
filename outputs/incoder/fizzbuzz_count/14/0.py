
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 13
        n //= 11
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 13
        n //= 11
    return count

def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_fast(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 13
        n //= 11
    return count

def fizz_buzz_iterative_faster(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_faster(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 13
        n //= 11
    return count

def fizz_buzz_iterative_fastest(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_fastest(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 13
        n //= 11
    return count

def fizz_buzz_iterative_fastest_2(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_fastest_2(3298)
    153
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 13
        n //= 11
    return count

def fizz_