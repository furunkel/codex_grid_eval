
def octuples_sum_to_hundred(l: list):
    """
    octuples_sum_to_hundred takes a list of integers as an input.
    it returns True if there are 8 distinct elements in the list that
    sum to hundred, and False otherwise.

    >>> octuples_sum_to_hundred([1, 2, -3, 7, 2, 7])
    False
    """
    return len(set(l)) >= 8 and sum(l) == 100


def is_prime(n: int):
    """
    is_prime takes an integer as an input.
    it returns True if the integer is a prime number, and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factors(n: int):
    """
    prime_factors takes an integer as an input.
    it returns a list of prime factors of the integer.

    >>> prime_factors(12)
    [2, 2, 3]
    >>> prime_factors(13)
    [13]
    """
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors


def is_palindrome(s: str):
    """
    is_palindrome takes a string as an input.
    it returns True if the string is a palindrome, and False otherwise.

    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    """
    return s == s[::-1]


def is_anagram(s1: str, s2: str):
    """
    is_anagram takes two strings as inputs.
    it returns True if the two strings are anagrams, and False otherwise.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("hello", "world")
    False
    """
    return sorted(s1) == sorted(s2)


def is_pangram(s: str):
    """
    is_pangram takes a string as an input.
    it returns True if the string is a pangram, and False otherwise.

    >>> is_pangram("The quick brown fox jumps over the lazy dog")
   