
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(50)
    2
    """
    if n%1837==0 or n%13==0:
        return 1
    else:
        return 0

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative(50)
    2
    """
    count = 0
    while n>0:
        if n%1837==0 or n%13==0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2(50)
    2
    """
    count = 0
    while n>0:
        if n%1837==0 or n%13==0:
            count += 1
        n //= 10
    return count

def fizz_buzz_iterative_v2_recursive(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2_recursive(50)
    2
    """
    if n == 0:
        return 0
    else:
        return fizz_buzz_iterative_v2_recursive(n//10)+1 if n%1837==0 or n%13==0 else 1

def fizz_buzz_iterative_v2_recursive_v2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v2(50)
    2
    """
    if n == 0:
        return 0
    else:
        return fizz_buzz_iterative_v2_recursive_v2(n//10)+1 if n%1837==0 or n%13==0 else 1

def fizz_buzz_iterative_v2_recursive_v3(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_v2_recursive_v3(50)
    2
    """
    if n == 0:
        return 0
    else:
        return fizz_buzz_iterative_v2_recursive_v3(n//10)+1 if n%1837==0 or n%13==0 else 1

def fizz_buzz_iterative_v2_recursive_v4(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 