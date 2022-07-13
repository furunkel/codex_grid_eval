
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    98
    """
    count = 0
    for i in range(1, n):
        if i % 13 == 0 or i % 3819 == 0:
            count += str(i).count('3')
    return count

def fizz_buzz_2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_2(3298)
    98
    """
    count = 0
    for i in range(1, n):
        if i % 13 == 0 or i % 3819 == 0:
            count += str(i).count('3')
    return count

def fizz_buzz_3(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_3(3298)
    98
    """
    count = 0
    for i in range(1, n):
        if i % 13 == 0 or i % 3819 == 0:
            count += str(i).count('3')
    return count

def fizz_buzz_4(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_4(3298)
    98
    """
    count = 0
    for i in range(1, n):
        if i % 13 == 0 or i % 3819 == 0:
            count += str(i).count('3')
    return count

def fizz_buzz_5(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_5(3298)
    98
    """
    count = 0
    for i in range(1, n):
        if i % 13 == 0 or i % 3819 == 0:
            count += str(i).count('3')
    return count

def fizz_buzz_6(n:int):
    """Return the number of times the