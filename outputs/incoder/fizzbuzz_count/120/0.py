
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz(50)
    3
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        elif n % 11 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_with_conditions(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_with_conditions(50)
    3
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        elif n % 11 == 0:
            count += 1
        elif n % 5 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_with_conditions_2(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_with_conditions_2(50)
    3
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        elif n % 11 == 0:
            count += 1
        elif n % 5 == 0:
            count += 1
        elif n % 3 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_with_conditions_3(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_with_conditions_3(50)
    3
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        elif n % 11 == 0:
            count += 1
        elif n % 5 == 0:
            count += 1
        elif n % 3 == 0:
            count += 1
        elif n % 2 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_with_conditions_4(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_with_conditions_4(50)
    3
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        elif n % 11 == 0:
            count += 1
        elif n % 5 == 0:
            count += 1
        elif n % 3 == 0:
            count += 1
        elif n % 2 == 0:
            count += 1
        elif n % 1 == 0:
            count += 1
        n //= 10
    return count

def fizz_buzz_with_conditions_5(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_with_conditions_5(50)
    3
    """
    count = 0
    while n > 0:
        if n % 13