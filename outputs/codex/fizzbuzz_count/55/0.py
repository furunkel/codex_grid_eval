
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz(78)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 7 == 0 or i % 13 == 0:
            count += str(i).count('4')
    return count

def fizz_buzz_2(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_2(78)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 7 == 0 or i % 13 == 0:
            count += str(i).count('4')
    return count

def fizz_buzz_3(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_3(78)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 7 == 0 or i % 13 == 0:
            count += str(i).count('4')
    return count

def fizz_buzz_4(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_4(78)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 7 == 0 or i % 13 == 0:
            count += str(i).count('4')
    return count

def fizz_buzz_5(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 7 or 13.
    >>> fizz_buzz_5(78)
    3
    """
    count = 0
    for i in range(1, n):
        if i % 7 == 0 or i % 13 == 0:
            count += str(i).count('4')
    return count

def fizz_buzz_6(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by