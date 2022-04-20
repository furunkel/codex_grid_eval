
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= -1 (and "neither" if -100 <= n < -1).
    """
    if n < -100:
        return "mouse"
    elif -100 <= n < -1:
        return "neither"
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
    return n % 2 == 1

def is_divisible_by_3(n):
    """
        Given an integer n, return True if n is divisible by 3 and False if n is not divisible by 3.
    """
    return n % 3 == 0

def is_divisible_by_5(n):
    """
        Given an integer n, return True if n is divisible by 5 and False if n is not divisible by 5.
    """
    return n % 5 == 0

def is_divisible_by_7(n):
    """
        Given an integer n, return True if n is divisible by 7 and False if n is not divisible by 7.
    """
    return n % 7 == 0

def is_divisible_by_9(n):
    """
        Given an integer n, return True if n is divisible by 9 and False if n is not divisible by 9.
    """
    return n % 9 == 0

def is_divisible_by_11(n):
    """
        Given an integer n, return True if n is divisible by 11 and False if n is not divisible by 11.
    """
    return n % 11 == 0

def is_divisible_by_13(n):
    """
        Given an integer n, return True if n is divisible by 13 and False if n is not divisible by 13.
    """
    return n % 13 == 0

def is_divisible_by_17(n):
    """
        Given an integer n, return True if n is divisible by 17 and False if n is not divisible by 17.
    """
    return n % 17