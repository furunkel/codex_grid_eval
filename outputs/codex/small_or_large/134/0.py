
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "house" if n >= 15 (and "neither" if 2 <= n < 15).
    """
    if n < 2:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return "neither"

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    return n % 2 == 0

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    return n % 2 == 1

def is_positive(n):
    """
        Given an integer n, return True if n is positive and False if n is negative.
    """
    return n > 0

def is_negative(n):
    """
        Given an integer n, return True if n is negative and False if n is positive.
    """
    return n < 0

def is_non_negative(n):
    """
        Given an integer n, return True if n is non-negative and False if n is negative.
    """
    return n >= 0

def is_non_positive(n):
    """
        Given an integer n, return True if n is non-positive and False if n is positive.
    """
    return n <= 0

def is_factor(f, n):
    """
        Given integers f and n, return True if f is a factor of n and False if f is not a factor of n.
    """
    return n % f == 0

def is_multiple(m, n):
    """
        Given integers m and n, return True if m is a multiple of n and False if m is not a multiple of n.
    """
    return m % n == 0

def is_leap_year(year):
    """
        Given an integer year, return True if year is a leap year and False if year is not a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_prime(n):
    """
        Given an integer n, return True if n is prime and False if n is not prime.
    """
    if n < 2:
       