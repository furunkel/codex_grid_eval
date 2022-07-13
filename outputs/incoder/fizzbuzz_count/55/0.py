
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz(78)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n /= 10
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative(78)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n /= 10
    return count

def fizz_buzz_iterative_v2(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2(78)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n /= 10
    return count

def fizz_buzz_iterative_v2_recursive(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive(78)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n /= 10
    return count

def fizz_buzz_iterative_v2_recursive_v2(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2(78)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n /= 10
    return count

def fizz_buzz_iterative_v2_recursive_v2_recursive(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2_recursive(78)
    3
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 13 == 0:
            count += 1
        n /= 10
    return count

def fizz_buzz_iterative_v2_recursive_v2_recursive_v2(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2_recursive_v2_recursive(