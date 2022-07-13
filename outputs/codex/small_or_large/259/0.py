
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2000 (and "None" if -100 <= n < 2000).
    """
    if n < -100:
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

def is_zero(n):
    """
        Given an integer n, return True if n is zero and False if n is non-zero.
    """
    return n == 0

def is_multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    return n % 5 == 0

def is_multiple_of_ten(n):
    """
        Given an integer n, return True if n is a multiple of 10 and False if n is not a multiple of 10.
    """
    return n % 10 == 0

def is_multiple_of_x(n, x):
    """
        Given an integer n and an integer x, return True if n is a multiple of x and False if n is not a multiple of x.
    """
    return n % x == 0

def is_less_than_x(n, x):
    """
        Given an integer n and an integer x, return True if n is less than x and False if n is greater than or equal to x.
    """