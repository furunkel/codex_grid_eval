
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
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

def is_prime(n):
    """
        Given an integer n, return True if n is prime and False if n is not prime.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_palindrome(s):
    """
        Given a string s, return True if s is a palindrome and False if s is not a palindrome.
    """
    return s == s[::-1]

def is_vowel(c):
    """
        Given a character c, return True if c is a vowel and False if c is not a vowel.
    """
    return c in "aeiou"

def is_consonant(c):
    """
        Given a character c, return True if c is a consonant and False if c is not a consonant.
    """
    return c not in "aeiou" and c.isalpha()

def is_lower(c):
    """
        Given a character c, return True if c is lowercase and False if c is not lowercase.
    """
    return c.islower()

def is_upper(c):
    """
        Given a character c, return True if c is uppercase and False if c is not uppercase.
    """
    return c.isupper()

def is_letter(c):
    """
        Given a character c, return True if c is a letter and False if c is not a letter.
    """
    return c.isalpha()

def is_digit(c):
   