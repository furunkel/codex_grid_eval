
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iter(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iter(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_gen(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_gen(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iter2(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iter2(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_gen2(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_gen2(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iter3(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iter3(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_gen3(n):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_gen3(3298)
    262
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iter4(n):
    """Return the number of times the digit 3 appears in 