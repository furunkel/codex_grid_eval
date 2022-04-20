
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "large"
    elif n >= 2000:
        return "small"
    else:
        return None

# print(small_or_large(1))
# print(small_or_large(2000))
# print(small_or_large(15))

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    if n % 2 == 0:
        return True
    else:
        return False

# print(is_even(1))
# print(is_even(2))

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    if n % 2 == 0:
        return False
    else:
        return True

# print(is_odd(1))
# print(is_odd(2))

def is_positive(n):
    """
        Given an integer n, return True if n is positive and False if n is negative.
    """
    if n > 0:
        return True
    else:
        return False

# print(is_positive(1))
# print(is_positive(-1))

def is_negative(n):
    """
        Given an integer n, return True if n is negative and False if n is positive.
    """
    if n < 0:
        return True
    else:
        return False

# print(is_negative(1))
# print(is_negative(-1))

def is_non_zero(n):
    """
        Given an integer n, return True if n is non-zero and False if n is zero.
    """
    if n != 0:
        return True
    else:
        return False

# print(is_non_zero(1))
# print(is_non_zero(0))

def is_multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    if n % 5 ==