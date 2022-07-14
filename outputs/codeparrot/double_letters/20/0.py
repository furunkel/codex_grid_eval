def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every exclamation point.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isupper())


def get_random_string(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_string_with_length(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_string_with_length_and_random_chars(length, random_chars=None):
    """
    Returns a random string of the specified length and random characters.
    """
    if random_chars is None:
        random_chars = get_random_string_with_length(length)
    return ''.join(random.choice(random_chars) for _ in range(length))


def get_random_string_with_length_and_random_chars_and_random_chars(length, random_chars=None, random_chars_and_random_chars=None):
    """
    Returns a random string of the specified length and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and