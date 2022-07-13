
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 10 and "small" if n >= 2000 (and "None" if 10 <= n < 2000).
    """
    if n < 10:
        return "large"
    elif n >= 2000:
        return "small"
    else:
        return "None"

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

def is_multiple_of_hundred(n):
    """
        Given an integer n, return True if n is a multiple of 100 and False if n is not a multiple of 100.
    """
    return n % 100 == 0

def is_multiple_of_thousand(n):
    """
        Given an integer n, return True if n is a multiple of 1000 and False if n is not a multiple of 1000.
    """
    return n % 1000 ==