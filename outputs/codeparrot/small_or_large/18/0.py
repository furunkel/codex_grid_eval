
def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 15 (and None if -100 <= n < 15).
    """

def is_prime(n):
    """
        Given an integer n, return True if n is prime, otherwise False.
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
    return True

def is_prime_factor(n):
    """
        Given an integer n, return True if n is prime factor, otherwise False.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    return True

def is_prime_divides(n):
    """
        Given an integer n, return True if n is prime divides n.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    return True

def is_prime_divisors(n):
    """
        Given an integer n, return True if n is prime divides n.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    return True

def is_prime_divisor_factor(n):
    """
        Given an integer n, return True if n is prime divides n.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    return True

def is_prime_divisor_divides(n):
    """
        Given an integer n, return True if n is prime divides n.
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if