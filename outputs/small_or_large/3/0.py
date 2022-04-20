
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return None

# print(small_or_large(1000))

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    if n % 2 == 0:
        return True
    else:
        return False

# print(is_even(5))

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    if n % 2 == 0:
        return False
    else:
        return True

# print(is_odd(5))

def is_positive(n):
    """
        Given an integer n, return True if n is positive and False if n is negative.
    """
    if n > 0:
        return True
    else:
        return False

# print(is_positive(5))

def is_negative(n):
    """
        Given an integer n, return True if n is negative and False if n is positive.
    """
    if n < 0:
        return True
    else:
        return False

# print(is_negative(5))

def is_non_zero(n):
    """
        Given an integer n, return True if n is non-zero and False if n is zero.
    """
    if n != 0:
        return True
    else:
        return False

# print(is_non_zero(5))

def is_multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False if n is not a multiple of 5.
    """
    if n % 5 == 0:
        return True
    else:
        return False

# print(is_multiple_of_five(5))

def is_three(n):
    """
        Given an integer n, return True if n is 3 and False if n is not 3.
    """
    if n == 3:
        return