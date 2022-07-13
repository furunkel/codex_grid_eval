
def small_or_large(n):
    """
        Given an integer n, return "large" if n < 2 and "small" if n >= 15 (and None if 2 <= n < 15).
    """
    if n < 2:
        return "large"
    elif n >= 15:
        return "small"
    else:
        return None

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

def is_non_negative(n):
    """
        Given an integer n, return True if n is non-negative and False if n is negative.
    """
    return n >= 0

def is_non_positive(n):
    """
        Given an integer n, return True if n is non-positive and False if n is positive.
    """
    return n <= 0

def is_factor(f, n):
    """
        Given integers f and n, return True if f is a factor of n and False if f is not a factor of n.
    """
    return n % f == 0

def is_multiple(m, n):
    """
        Given integers m and n, return True if m is a multiple of n and False if m is not a multiple of n.
    """
    return m % n == 0

def fizzbuzz(n):
    """
        Given an integer n, return "fizz" if n is divisible by 3, "buzz" if n is divisible by 5, and "fizzbuzz" if n is divisible by both 3 and 5.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n %