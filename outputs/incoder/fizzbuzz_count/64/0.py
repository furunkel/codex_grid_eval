
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(78)
    0
    """
    if n%1837 == 0 or n%13 == 0:
        return 0
    else:
        return 1

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative(78)
    0
    """
    count = 0
    while n%1837 == 0 or n%13 == 0:
        count += 1
        n //= 1837
    return count

def fizz_buzz_iterative_v2(n):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2(78)
    0
    """
    count = 0
    while n%1837 == 0 or n%13 == 0:
        count += 1
        n //= 1837
    return count

def fizz_buzz_iterative_v2_recursive(n):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2_recursive(78)
    0
    """
    if n == 0:
        return 0
    else:
        return fizz_buzz_iterative_v2_recursive(n//1837) + fizz_buzz_iterative_v2_recursive(n//13)

def fizz_buzz_iterative_v2_recursive_v2(n):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2(78)
    0
    """
    if n == 0:
        return 0
    else:
        return fizz_buzz_iterative_v2_recursive_v2(n//1837) + fizz_buzz_iterative_v2_recursive_v2(n//13)

def fizz_buzz_iterative_v2_recursive_v2_recursive(n):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2_recursive(78)
    0
    """
    if n == 0:
        return 0
    else:
        return fizz_buzz_iterative_v2_recursive_v2_recursive(n//1837) + fizz_buzz_iterative_v2_recursive_v2_recursive(n//13)

def fizz_buzz_iterative_v2_recursive_v2_recursive_v2(n):
    """Return the number of times the digit 4 appear