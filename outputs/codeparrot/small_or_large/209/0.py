
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "small" if n >= 2 (and None if -100 <= n < 2).
    """

def is_prime(n):
    """
        Given an integer n, return True if n is prime.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n % 11 == 0:
        return False
    return True

def is_prime_factor(n):
    """
        Given an integer n, return True if n is prime factor.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n % 11 == 0:
        return False
    return True

def is_prime_divides(n):
    """
        Given an integer n, return True if n is prime divides.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n % 11 == 0:
        return False
    return True

def is_prime_divisors(n):
    """
        Given an integer n, return True if n is prime divides with remainder.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    if n % 11 == 0:
        return False
    return True

def is_prime_divisor_factor(n):
    """
        Given an integer n, return True if n is prime divides with remainder.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False