
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "small" if n >= 2 (and "None" if -100 <= n < 2).
    """
    if n < -100:
        return "large"
    elif -100 <= n < 2:
        return "None"
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
        Given an integer n, return True if n