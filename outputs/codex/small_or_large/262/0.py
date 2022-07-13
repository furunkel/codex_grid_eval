
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 2 and "house" if n >= 15 (and "None" if 2 <= n < 15).
    """
    if n < 2:
        return "large"
    elif n >= 15:
        return "house"
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

def is_non_zero(n):
    """
        Given an integer n, return True if n is non-zero and False if n is zero.
    """
    return n != 0

def multiple_of_5(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    return n % 5 == 0

def multiple_of_3_and_5(n):
    """
        Given an integer n, return True if n is a multiple of 3 and 5 and False if n is not a multiple of 3 and 5.
    """
    return n % 3 == 0 and n % 5 == 0

def multiple_of_3_or_5(n):
    """
        Given an integer n, return True if n is a multiple of 3 or 5 and False if n is not a multiple of 3 or 5.
    """
    return n % 3 == 0 or n % 5 == 0

def multiple_of_3_and_5_but_not_both(n):
    """
        Given an integer n, return True if n is a multiple of 3 and 5 but not both and False if n is not a multiple of 3 and 5 but not both.
    """
    return (n % 3 == 0 and n % 5 !=