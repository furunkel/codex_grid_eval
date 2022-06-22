
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(3298)
    331
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('1')
    return count

def fizz_buzz_2(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_2(3298)
    331
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('1')
    return count

def fizz_buzz_3(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_3(3298)
    331
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('1')
    return count

def fizz_buzz_4(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_4(3298)
    331
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('1')
    return count

def fizz_buzz_5(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_5(3298)
    331
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('1')
    return count

def fizz_buzz_6(n:int):
    """Return the number of times the digit 1 appears in integers less than n which