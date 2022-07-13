
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz(3298)
    159
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 13
        n //= 3819
    return count

def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative(3298)
    159
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 13
        n //= 3819
    return count

def fizz_buzz_iterative_memoized(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_iterative_memoized(3298)
    159
    """
    count = 0
    memo = {}
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 13
        n //= 3819
        if n in memo:
            count = memo[n]
        memo[n] = count
    return count

def fizz_buzz_memoized(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_memoized(3298)
    159
    """
    memo = {}
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 13
        n //= 3819
        if n in memo:
            count = memo[n]
        memo[n] = count
    return count

def fizz_buzz_memoized_iterative(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 13 or 3819.
    >>> fizz_buzz_memoized_iterative(3298)
    159
    """
    memo = {}
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 3819 == 0:
            count += 1
        n //= 13
        n //= 3819
        if n in memo:
            count = memo[n]
        memo[n] = count
    return count

def fizz_buzz_memoized_iterative_memoized(n:int):
    """Return the number of times the digit 1 appears in integers less than n 