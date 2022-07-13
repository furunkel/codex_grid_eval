
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < -100:
        return "mouse"
    elif -100 <= n < -1:
        return None
    else:
        return "small"

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

def is_multiple_of_6(n):
    """
        Given an integer n, return True if n is a multiple of 6 and False if n is not a multiple of 6.
    """
    return n % 6 == 0

def is_multiple_of_both_5_and_6(n):
    """
        Given an integer n, return True if n is a multiple of both 5 and 6 and False if n is not a multiple of both 5 and 6.
    """
    return n % 5 == 0 and n % 6 == 0

def is_multiple_of_either_5_or_6(n):
    """
        Given an integer n, return True if n is