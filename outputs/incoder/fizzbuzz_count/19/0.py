
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz(78)
    4
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        elif n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative(78)
    4
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        elif n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fast(78)
    4
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        elif n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast2(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fast2(78)
    4
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        elif n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast3(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fast3(78)
    4
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        elif n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast4(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fast4(78)
    4
    """
    count = 0
    while n > 0:
        if n % 7 == 0:
            count += 1
        elif n % 13 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_fast5(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_fast5(78)
    4
    """
    count = 0
    while n > 0: