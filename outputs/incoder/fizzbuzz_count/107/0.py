
def fizz_buzz(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 3819.
    >>> fizz_buzz(3298)
    1
    """
    count = 0
    while n >= 1837 and n <= 3819:
        if n % 1837 == 0 and n % 3819 == 0:
            count += 1
        n /= 1837
        n /= 3819
    return count


def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 3819.
    >>> fizz_buzz_iterative(3298)
    1
    """
    count = 0
    while n >= 1837 and n <= 3819:
        if n % 1837 == 0 and n % 3819 == 0:
            count += 1
        n /= 1837
        n /= 3819
    return count


def fizz_buzz_iterative_v2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 3819.
    >>> fizz_buzz_iterative_v2(3298)
    1
    """
    count = 0
    while n >= 1837 and n <= 3819:
        if n % 1837 == 0 and n % 3819 == 0:
            count += 1
        n /= 1837
        n /= 3819
    return count


def fizz_buzz_iterative_v2_recursive(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 3819.
    >>> fizz_buzz_iterative_v2_recursive(3298)
    1
    """
    count = 0
    while n >= 1837 and n <= 3819:
        if n % 1837 == 0 and n % 3819 == 0:
            count += 1
        n /= 1837
        n /= 3819
    return count


def fizz_buzz_iterative_v2_recursive_v2(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 3819.
    >>> fizz_buzz_iterative_v2_recursive_v2(3298)
    1
    """
    count = 0
    while n >= 1837 and n <= 3819:
        if n % 1837 == 0 and n % 3819 == 0:
            count += 1
        n /= 1837
        n /= 3819
    return count


def fizz_buzz_iterative_v2_recursive_v2_recursive(n:int):
    """Return the number of times the digit 3 appears in integers less than n which are divisible by 1837 or 3819.
    >>> fizz_buzz_iterative_v2_recursive_v2_recursive(3298)
    1
    """
