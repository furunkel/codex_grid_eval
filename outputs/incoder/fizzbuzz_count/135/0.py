
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(50)
    1
    """
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n%1837==0 or n%13==0:
        return fizz_buzz(n//10)+1
    else:
        return fizz_buzz(n//10)

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative(50)
    1
    """
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n%1837==0 or n%13==0:
        return fizz_buzz_iterative(n//10)+1
    else:
        return fizz_buzz_iterative(n//10)

def fizz_buzz_iterative_fast(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fast(50)
    1
    """
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n%1837==0 or n%13==0:
        return fizz_buzz_iterative_fast(n//10)+1
    else:
        return fizz_buzz_iterative_fast(n//10)

def fizz_buzz_iterative_fast2(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fast2(50)
    1
    """
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n%1837==0 or n%13==0:
        return fizz_buzz_iterative_fast2(n//10)+1
    else:
        return fizz_buzz_iterative_fast2(n//10)

def fizz_buzz_iterative_fast3(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_iterative_fast3(50)
    1
    """
    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    if n%1837==0 or n%13==0:
        return fizz_buzz_iterative_fast3(n//10)+1
    else:
        return fizz_buzz_iterative_fast3(n//10)

def fizz_buzz_iterative_fast