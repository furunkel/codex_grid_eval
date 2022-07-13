
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "large"
    elif n >= 2000:
        return "house"
    else:
        return None

def is_prime(n):
    """
        Given an integer n, return True if n is prime and False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_even(n):
    """
        Given an integer n, return True if n is even and False otherwise.
    """
    return n % 2 == 0

def is_odd(n):
    """
        Given an integer n, return True if n is odd and False otherwise.
    """
    return n % 2 == 1

def is_multiple_of_3(n):
    """
        Given an integer n, return True if n is a multiple of 3 and False otherwise.
    """
    return n % 3 == 0

def is_multiple_of_5(n):
    """
        Given an integer n, return True if n is a multiple of 5 and False otherwise.
    """
    return n % 5 == 0

def is_multiple_of_7(n):
    """
        Given an integer n, return True if n is a multiple of 7 and False otherwise.
    """
    return n % 7 == 0

def is_multiple_of_11(n):
    """
        Given an integer n, return True if n is a multiple of 11 and False otherwise.
    """
    return n % 11 == 0

def is_multiple_of_13(n):
    """
        Given an integer n, return True if n is a multiple of 13 and False otherwise.
    """
    return n % 13 == 0

def is_multiple_of_17(n):
    """
        Given an integer n, return True if n is a multiple of 17 and False otherwise.
    """
    return n % 17 == 0

def is_multiple_of_19(n):
    """
        Given an integer n, return True if n is a multiple of 19 and False otherwise.
    """
    return n