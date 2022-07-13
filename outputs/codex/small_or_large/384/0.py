
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < -100:
        return "mouse"
    elif n >= -100 and n < -1:
        return None
    else:
        return "house"

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    if n % 2 == 0:
        return False
    else:
        return True

def is_positive(n):
    """
        Given an integer n, return True if n is positive and False if n is negative.
    """
    if n > 0:
        return True
    else:
        return False

def is_negative(n):
    """
        Given an integer n, return True if n is negative and False if n is positive.
    """
    if n < 0:
        return True
    else:
        return False

def is_non_zero(n):
    """
        Given an integer n, return True if n is non-zero and False if n is zero.
    """
    if n != 0:
        return True
    else:
        return False

def is_multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    if n % 5 == 0:
        return True
    else:
        return False

def is_multiple_of_ten(n):
    """
        Given an integer n, return True if n is a multiple of 10 and False if n is not a multiple of 10.
    """
    if n % 10 == 0:
        return True
    else:
        return False

def is_multiple_of_hundred(n):
    """
        Given an integer n, return True if n is a multiple of 100 and False if n is not a multiple of 100.
    """
    if n % 100 == 0:
       