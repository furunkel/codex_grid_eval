
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "large" if n >= 15 (and "neither" if 10 <= n < 15).
    """
    if n < 10:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return "neither"

def is_even(n):
    """
        Given an integer n, return True if n is even and False if n is odd.
    """
    return n % 2 == 0

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False if n is even.
    """
    return n % 2 == 1

def is_factor(f, n):
    """
        Given integers f and n, return True if f is a factor of n and False otherwise.
    """
    return n % f == 0

def is_multiple(m, n):
    """
        Given integers m and n, return True if m is a multiple of n and False otherwise.
    """
    return m % n == 0

def f2c(t):
    """
        Given an integer representing a temperature in Fahrenheit degrees, return the temperature in Celsius degrees.
    """
    return (t - 32) * 5 / 9

def c2f(t):
    """
        Given an integer representing a temperature in Celsius degrees, return the temperature in Fahrenheit degrees.
    """
    return t * 9 / 5 + 32

def f2k(t):
    """
        Given an integer representing a temperature in Fahrenheit degrees, return the temperature in Kelvin degrees.
    """
    return (t - 32) * 5 / 9 + 273.15

def c2k(t):
    """
        Given an integer representing a temperature in Celsius degrees, return the temperature in Kelvin degrees.
    """
    return t + 273.15

def k2f(t):
    """
        Given an integer representing a temperature in Kelvin degrees, return the temperature in Fahrenheit degrees.
    """
    return (t - 273.15) * 9 / 5 + 32

def k2c(t):
    """
        Given an integer representing a temperature in Kelvin degrees, return the temperature in Celsius degrees.
    """
    return t - 273.15

def hypotenuse(a, b):
    """
        Given integers a and b,