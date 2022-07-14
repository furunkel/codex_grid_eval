def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return "".join([c for c in string if c.isalpha()])


def get_all_letters(string):
    """
    Given a string, return all the letters in the string.
    """
    return "".join([c for c in string if c.isalpha()])


def get_all_letters_and_numbers(string):
    """
    Given a string, return all the letters and numbers in the string.
    """
    return "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isdigit()])


def get_all_letters_and_numbers_and_letters(string):
    """
    Given a string, return all the letters and numbers in the string.
    """
    return "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isdigit()]) + "".join([c for c in string if c.isalpha()])


def get_all_letters_and_numbers_and_letters_and_numbers(string):
    """
    Given a string, return all the letters and numbers in the string.
    """
    return "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isdigit()]) + "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isalpha()])


def get_all_letters_and_numbers_and_letters_and_numbers_and_letters(string):
    """
    Given a string, return all the letters and numbers in the string.
    """
    return "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isdigit()]) + "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isalpha()]) + "".join([c for c in string if c.isalpha()])


def get_all_letters_and_numbers_and_letters_and_letters_and_numbers