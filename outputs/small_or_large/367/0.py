
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "small" if n >= 2000 (and "None" if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n >= 2000:
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

def f2c(t):
    """
        Given a temperature t in degrees Fahrenheit, return the corresponding temperature in degrees Celsius.
    """
    return (t - 32) * 5 / 9

def c2f(t):
    """
        Given a temperature t in degrees Celsius, return the corresponding temperature in degrees Fahrenheit.
    """
    return t * 9 / 5 + 32

def test(got, expected):
    """
        Simple test() function used in main() to print what