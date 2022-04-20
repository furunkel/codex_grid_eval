
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 1000 and "small" if n >= 2000 (and None if 1000 <= n < 2000).
    """
    if n < 1000:
        return "large"
    elif n >= 2000:
        return "small"
    else:
        return None

# print(small_or_large(1000))
# print(small_or_large(1001))
# print(small_or_large(999))

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

def is_multiple_of_three(n):
    """
        Given an integer n, return True if n is a multiple of three and False if n is not a multiple of three.
    """
    if n % 3 == 0:
        return True
    else:
        return False

# print(is_multiple_of_three(3))
# print(is_multiple_of_three(4))

def is_multiple_of_five(n):
    """
        Given an integer n, return True if n is a multiple of five and False if n is not a multiple of five.
    """
    if n % 5 == 0:
        return True
    else:
        return False

# print(is_multiple_of_five(5))
# print(is_multiple_of_five(4))

def is_multiple_of_six(n):
    """
        Given an integer n, return True if n is a multiple of six and False if n is not a multiple of six.
    """
    if n % 6 == 0:
        return True
    else:
        return False

# print(is_multiple_of_six(6))
# print(is_multiple_of_six(