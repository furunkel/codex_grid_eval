
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz(50)
    0
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
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative(50)
    0
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_v2(50)
    0
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2_recursive(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_v2_recursive(50)
    0
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2_recursive_v2(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_v2_recursive_v2(50)
    0
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2_recursive_v3(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_v2_recursive_v3(50)
    0
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2_recursive_v4(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_