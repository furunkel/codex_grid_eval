
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= -1 (and "neither" if -100 <= n < -1).
    """
    if n < -100:
        return "small"
    elif n >= -1:
        return "house"
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

def is_multiple_of_5(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    return n % 5 == 0

def is_multiple_of_10(n):
    """
        Given an integer n, return True if n is a multiple of 10 and False if n is not a multiple of 10.
    """
    return n % 10 == 0

def is_multiple_of_100(n):
    """
        Given an integer n, return True if n is a multiple of 100 and False if n is not a multiple of 100.
    """
    return n % 100 == 0

def is_multiple_of_1000(n):
    """
        Given an integer n, return True if n is a multiple of 1000 and False if n is not a multiple of 1000.
    """
    return n % 1000