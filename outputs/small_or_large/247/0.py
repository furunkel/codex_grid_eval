
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 2 and "house" if n >= 2000 (and None if 2 <= n < 2000).
    """
    if n < 2:
        return "large"
    elif n >= 2000:
        return "house"
    else:
        return None

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

def is_non_zero(n):
    """
        Given an integer n, return True if n is non-zero and False if n is zero.
    """
    return n != 0

def multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    return n % 5 == 0

def multiple_of_ten(n):
    """
        Given an integer n, return True if n is a multiple of 10 and False if n is not a multiple of 10.
    """
    return n % 10 == 0

def multiple_of_x(n, x):
    """
        Given two integers n and x, return True if n is a multiple of x and False if n is not a multiple of x.
    """
    return n % x == 0

def is_leap_year(year):
    """
        Given a year, return True if it is a leap year and False if it is not a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_vowel(letter):
    """
        Given a letter, return True if it is a vowel and False if it is not a vowel.
    """
