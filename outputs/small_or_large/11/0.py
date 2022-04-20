
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "small"
    elif n >= 2000:
        return "large"
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

def is_divisible_by_three(n):
    """
        Given an integer n, return True if n is divisible by 3 and False if n is not.
    """
    if n % 3 == 0:
        return True
    else:
        return False

# print(is_divisible_by_three(1))
# print(is_divisible_by_three(3))

def is_divisible_by_five(n):
    """
        Given an integer n, return True if n is divisible by 5 and False if n is not.
