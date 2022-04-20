
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= 15 (and "neither" if -100 <= n < 15).
    """
    if n < -100:
        return "mouse"
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
    return n % 11 ==