
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "small" if n >= 2000 (and "None" if -100 <= n < 2000).
    """
    if n < -100:
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


def is_multiple_of_three(n):
    """
        Given an integer n, return True if n is a multiple of 3 and False if n is not a multiple of 3.
    """
    return n % 3 == 0


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


def is_multiple_of_y(n, y):
    """
        Given an integer n and an integer y, return True if n is a multiple of y and False if n is not a multiple of y.
    """
    return n % y == 0


def is_multiple_of_x_and_y(n, x, y):
    """
        Given an integer n, an integer x, and an integer y, return True if n is a multiple of x and y and False if n is not a multiple of x and y.
    """
    return n % x == 0 and n % y == 0


def is_multiple_of_x_or_y(n, x, y):
    """
