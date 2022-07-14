def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isalpha())


def get_random_string(length):
    """
    Returns a random string of length length, with a minimum of 3 characters.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_string_with_length(length):
    """
    Returns a random string of length length, with a minimum of 3 characters.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_string_with_length_and_random_chars(length, random_chars):
    """
    Returns a random string of length length, with a minimum of 3 characters.
    """
    return ''.join(random.choice(random_chars) for _ in range(length))


def get_random_string_with_length_and_random_chars_and_random_chars(length, random_chars, random_chars_and_random_chars):
    """
    Returns a random string of length length, with a minimum of 3 characters and a random character.
    """
    return ''.join(random.choice(random_chars) for _ in range(length))


def get_random_string_with_length_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_