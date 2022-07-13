
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz(3298)
    203
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 7
        n //= 13
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative(3298)
    203
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 7
        n //= 13
    return count

def fizz_buzz_iterative_v2(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2(3298)
    203
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 7
        n //= 13
    return count

def fizz_buzz_iterative_v2_recursive(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive(3298)
    203
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 7
        n //= 13
    return count

def fizz_buzz_iterative_v2_recursive_v2(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2(3298)
    203
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 7
        n //= 13
    return count

def fizz_buzz_iterative_v2_recursive_v2_recursive(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2_recursive(3298)
    203
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        if n % 13 == 0:
            count += 1
        n //= 7
        n //= 