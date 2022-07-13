
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(3298)
    331
    """
    if n%11==0 and n%13==0:
        return 1
    elif n%11==0:
        return fizz_buzz(n//11)
    elif n%13==0:
        return fizz_buzz(n//13)
    else:
        return 0
</cell>
<cell>
fizz_buzz(3298)
</cell>
<cell>
def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative(3298)
    331
    """
    count=0
    while n>0:
        if n%11==0 and n%13==0:
            count+=1
        elif n%11==0:
            n//=11
        elif n%13==0:
            n//=13
        else:
            n=0
    return count
</cell>
<cell>
fizz_buzz_iterative(3298)
</cell>
<cell>
def fizz_buzz_iterative_v2(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative_v2(3298)
    331
    """
    count=0
    while n>0:
        if n%11==0 and n%13==0:
            count+=1
        elif n%11==0:
            count+=fizz_buzz_iterative_v2(n//11)
        elif n%13==0:
            count+=fizz_buzz_iterative_v2(n//13)
        else:
            n=0
    return count
</cell>
<cell>
fizz_buzz_iterative_v2(3298)
</cell>
<cell>
def fizz_buzz_iterative_v2_recursive(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz_iterative_v2_recursive(3298)
    331
    """
    count=0
    if n>0:
        if n%11==0 and n%13==0:
            count+=1
        elif n%11==0:
            count+=fizz_buzz_iterative_v2_recursive(n//11)
        elif n%13==0:
            count+=fizz_buzz_iterative_v2_recursive(n//13)
        else:
            n=0
    return count
</