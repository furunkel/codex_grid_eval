def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isupper())


def get_random_string(length):
    """
    Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_length(length):
    """
    Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_random_chars(length):
    """
    Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_random_chars_and_length(length):
    """
    Returns a random string of length length and random chars.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_random_chars_and_length_and_random_chars(length, random_chars):
    """
    Returns a random string of length length and random chars.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_random_chars_and_length_and_random_chars_and_random_chars_and_random_chars(length, random_chars, random_chars_and_length):
    """
    Returns a random string of length length and random chars.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars_and_random_chars