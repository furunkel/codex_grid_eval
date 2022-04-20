
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "house" if n >= 2000 (and "neither" if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n >= 2000:
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

def is_multiple_of_3(n):
    """
        Given an integer n, return True if n is a multiple of 3 and False if n is not a multiple of 3.
    """
    return n % 3 == 0

def is_multiple_of_5(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    return n % 5 == 0

def is_multiple_of_7(n):
    """
        Given an integer n, return True if n is a multiple of 7 and False if n is not a multiple of 7.
    """
    return n % 7 == 0

def is_multiple_of_11(n):
    """
        Given an integer n, return True if n is a multiple of 11 and False if n is not a multiple of 11.
    """
    return n % 11 == 0