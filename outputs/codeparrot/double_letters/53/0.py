def double_letters(string):
    """
    Given a string, return the string, doubling every vowel (lower-case or upper-case) character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return "".join(c for c in string if c.isalpha())


def get_all_letters():
    """
    Returns a list of all the letters in the alphabet.
    """
    return [c for c in alphabet if c.isalpha()]


def get_all_letters_with_vowels():
    """
    Returns a list of all the letters in the alphabet with vowels.
    """
    return [c for c in alphabet if c.isalpha() and c.isupper()]


def get_all_letters_with_letters():
    """
    Returns a list of all the letters in the alphabet with letters.
    """
    return [c for c in alphabet if c.isalpha() and c.isupper()]


def get_all_letters_with_letters_with_vowels():
    """
    Returns a list of all the letters in the alphabet with letters and vowels.
    """
    return [c for c in alphabet if c.isalpha() and c.isupper() and c.isalpha()]


def get_all_letters_with_letters_with_letters_with_vowels():
    """
    Returns a list of all the letters in the alphabet with letters and vowels.
    """
    return [c for c in alphabet if c.isalpha() and c.isupper() and c.isalpha()]


def get_all_letters_with_letters_with_letters_with_vowels_and_letters():
    """
    Returns a list of all the letters in the alphabet with letters and vowels and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and letters and