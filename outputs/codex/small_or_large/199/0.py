
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 2 and "small" if n >= 2000 (and None if 2 <= n < 2000).
    """
    if n < 2:
        return "large"
    elif n >= 2000:
        return "small"
    else:
        return None

# print(small_or_large(1))
# print(small_or_large(2000))
# print(small_or_large(1000))

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    return n % 2 == 0

# print(is_even(2))
# print(is_even(3))

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    return n % 2 != 0

# print(is_odd(2))
# print(is_odd(3))

def is_positive(n):
    """
        Given an integer n, return True if n is positive and False if n is negative.
    """
    return n > 0

# print(is_positive(2))
# print(is_positive(-2))

def is_negative(n):
    """
        Given an integer n, return True if n is negative and False if n is positive.
    """
    return n < 0

# print(is_negative(2))
# print(is_negative(-2))

def is_non_zero(n):
    """
        Given an integer n, return True if n is non-zero and False if n is zero.
    """
    return n != 0

# print(is_non_zero(2))
# print(is_non_zero(0))

def is_multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    return n % 5 == 0

# print(is_multiple_of_five(2))
# print(is_multiple_of_five(5))

def is_three(n):
    """
        Given an integer n, return True if n is 3 and False if n is not 3.
   