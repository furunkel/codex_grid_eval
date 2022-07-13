
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "small" if n >= 15 (and None if -100 <= n < 15).
    """
    if n < -100:
        return "large"
    elif n >= 15:
        return "small"
    else:
        return None

# print(small_or_large(15))
# print(small_or_large(-101))
# print(small_or_large(14))

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    if n % 2 == 0:
        return True
    else:
        return False

# print(is_even(2))
# print(is_even(3))

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    if n % 2 == 0:
        return False
    else:
        return True

# print(is_odd(2))
# print(is_odd(3))

def is_positive(n):
    """
        Given an integer n, return True if n is positive and False if n is negative.
    """
    if n > 0:
        return True
    else:
        return False

# print(is_positive(2))
# print(is_positive(-2))

def is_negative(n):
    """
        Given an integer n, return True if n is negative and False if n is positive.
    """
    if n < 0:
        return True
    else:
        return False

# print(is_negative(2))
# print(is_negative(-2))

def is_divisible_by_3(n):
    """
        Given an integer n, return True if n is divisible by 3 and False if n is not divisible by 3.
    """
    if n % 3 == 0:
        return True
    else:
        return False

# print(is_divisible_by_3(3))
# print(is_divisible_by_3(4))

def is_divisible_by_5(n):
    """
        Given an integer n, return True if n is divisible by 5 and False if