
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 1000 and "house" if n >= 2000 (and None if 1000 <= n < 2000).
    """
    if n < 1000:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return None

def is_prime(n):
    """
        Given an integer n, return True if n is a prime number and False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_palindrome(s):
    """
        Given a string s, return True if s is a palindrome and False otherwise.
    """
    return s == s[::-1]

def is_vowel(c):
    """
        Given a character c, return True if c is a vowel and False otherwise.
    """
    return c in "aeiou"

def is_consonant(c):
    """
        Given a character c, return True if c is a consonant and False otherwise.
    """
    return c not in "aeiou" and c.isalpha()

def is_digit(c):
    """
        Given a character c, return True if c is a digit and False otherwise.
    """
    return c.isdigit()

def is_lower(c):
    """
        Given a character c, return True if c is a lowercase letter and False otherwise.
    """
    return c.islower()

def is_upper(c):
    """
        Given a character c, return True if c is an uppercase letter and False otherwise.
    """
    return c.isupper()

def is_letter(c):
    """
        Given a character c, return True if c is a letter and False otherwise.
    """
    return c.isalpha()

def is_alphanumeric(c):
    """
        Given a character c, return True if c is an alphanumeric character and False otherwise.
    """
    return c.isalnum()

def is_whitespace(c):
    """
        Given a character c, return True if c is a whitespace character and False otherwise.
    """
    return c.