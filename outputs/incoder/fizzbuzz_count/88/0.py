
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(78)
    2
    """
    count = 0
    while n >= 13:
        if n % 13 == 0:
            count += 1
        n /= 13
    while n >= 3819:
        if n % 3819 == 0:
            count += 1
        n /= 3819
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative(78)
    2
    """
    count = 0
    while n >= 13:
        if n % 13 == 0:
            count += 1
        n /= 13
    while n >= 3819:
        if n % 3819 == 0:
            count += 1
        n /= 3819
    return count

def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast(78)
    2
    """
    count = 0
    while n >= 13:
        if n % 13 == 0:
            count += 1
        n /= 13
    while n >= 3819:
        if n % 3819 == 0:
            count += 1
        n /= 3819
    return count

def fizz_buzz_iterative_fast2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast2(78)
    2
    """
    count = 0
    while n >= 13:
        if n % 13 == 0:
            count += 1
        n /= 13
    while n >= 3819:
        if n % 3819 == 0:
            count += 1
        n /= 3819
    return count

def fizz_buzz_iterative_fast3(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast3(78)
    2
    """
    count = 0
    while n >= 13:
        if n % 13 == 0:
            count += 1
        n /= 13
    while n >= 3819:
        if n % 3819 == 0:
            count += 1
        n /= 3819
    return count

def fizz_buzz_iterative_fast4(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_fast4(78)
    2
    """
    count = 0
    while n >= 13:
        if n % 13 == 0:
            count += 1
        n /= 13
