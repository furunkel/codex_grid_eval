
def fizz_buzz(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz(3298)
    151
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative(3298)
    151
    """
    count = 0
    while n > 0:
        if n % 13 == 0:
            count += 1
        if n % 11 == 0:
            count += 1
        n //= 10
    return count


def fizz_buzz_iterative_memoized(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_iterative_memoized(3298)
    151
    """
    count = 0
    memo = {}
    while n > 0:
        if n in memo:
            count = memo[n]
        else:
            if n % 13 == 0:
                count += 1
            if n % 11 == 0:
                count += 1
            memo[n] = count
        n //= 10
    return count


def fizz_buzz_memoized(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_memoized(3298)
    151
    """
    count = 0
    memo = {}
    while n > 0:
        if n in memo:
            count = memo[n]
        else:
            if n % 13 == 0:
                count += 1
            if n % 11 == 0:
                count += 1
            memo[n] = count
        n //= 10
    return count


def fizz_buzz_memoized_iterative(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_memoized_iterative(3298)
    151
    """
    count = 0
    memo = {}
    while n > 0:
        if n in memo:
            count = memo[n]
        else:
            if n % 13 == 0:
                count += 1
            if n % 11 == 0:
                count += 1
            memo[n] = count
        n //= 10
    return count


def fizz_buzz_memoized_iterative_memoized(n:int):
    """Return the number of times the digit 4 appears in integers less than n which are divisible by 13 or 11.
    >>> fizz_buzz_memoized_iterative_memoized(3298)
    151
    """
    count = 0