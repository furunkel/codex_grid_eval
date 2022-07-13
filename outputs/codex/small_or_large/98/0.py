
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= 15 (and None if -100 <= n < 15).
    """
    if n < -100:
        return "small"
    elif n >= 15:
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
    return n % 2 != 0

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
        Given an integer year, return True if year is a leap year and False if year is not a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_vowel(letter):
    """
        Given a string letter, return True if letter is a vowel and False if letter is not a vowel.
