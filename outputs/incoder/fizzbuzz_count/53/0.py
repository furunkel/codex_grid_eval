
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    73
    """
    if n%13 == 0 and n%3819 == 0:
        return 1
    else:
        return 0
</cell>
<cell>
# Solution 2
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    73
    """
    if n%13 == 0 and n%3819 == 0:
        return 1
    elif n%13 == 0:
        return fizz_buzz(n//13)
    elif n%3819 == 0:
        return fizz_buzz(n//3819)
    else:
        return 0
</cell>
<cell>
# Solution 3
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    73
    """
    if n%13 == 0 and n%3819 == 0:
        return 1
    elif n%13 == 0:
        return fizz_buzz(n//13)
    elif n%3819 == 0:
        return fizz_buzz(n//3819)
    else:
        return fizz_buzz(n//3819) + fizz_buzz(n//13)
</cell>
<cell>
# Solution 4
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    73
    """
    if n%13 == 0 and n%3819 == 0:
        return 1
    elif n%13 == 0:
        return fizz_buzz(n//13)
    elif n%3819 == 0:
        return fizz_buzz(n//3819)
    else:
        return fizz_buzz(n//3819) + fizz_buzz(n//13)
</cell>
<cell>
# Solution 5
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    73
    """
    if n%13 == 0 and n%3819 == 0:
        return 1
    elif n%13 == 0:
        return fizz_buzz(n//13)
    elif n%3819 == 0:
        return fizz_buzz(n//3819)
    else:
        return fizz_buzz(n//3819