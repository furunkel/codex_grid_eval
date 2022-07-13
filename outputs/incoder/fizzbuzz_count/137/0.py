
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(3298)
    160
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        count += 1
        n //= 13
    return count


def fizz_buzz_with_fizz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_with_fizz(3298)
    160
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        count += 1
        n //= 13
        if n % 5 == 0:
            count += 1
            n //= 5
    return count


def fizz_buzz_with_fizzbuzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_with_fizzbuzz(3298)
    160
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        count += 1
        n //= 13
        if n % 5 == 0:
            count += 1
            n //= 5
            if n % 3 == 0:
                count += 1
                n //= 3
    return count


def fizz_buzz_with_fizzbuzzbuzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_with_fizzbuzzbuzz(3298)
    160
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        count += 1
        n //= 13
        if n % 5 == 0:
            count += 1
            n //= 5
            if n % 3 == 0:
                count += 1
                n //= 3
                if n % 5 == 0:
                    count += 1
                    n //= 5
    return count


def fizz_buzz_with_fizzbuzzbuzzbuzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz_with_fizzbuzzbuzzbuzz(3298)
    160
    """
    count = 0
    while n >= 1837 or n % 13 == 0:
        count += 1
        n //= 13
        if n % 5 == 0:
            count += 1
            n //= 5
            if n % 3 == 0:
                count += 1
                n //= 3
                if n % 5 == 0:
                    count += 1
                    n //= 5
                    if n % 3 == 0:
                        count += 1
                        n //= 3
    return count


def fiz