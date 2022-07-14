def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every letter.
    All other characters should be output a single time each.
    """
    return ''.join(filter(lambda x: x in string, string))


def get_random_string(length):
    """
    Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_string_with_length(length):
    """
    Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_string_with_length_and_random_chars(length, random_chars):
    """
    Returns a random string of length length and random chars.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length)) + random_chars


def get_random_string_with_length_and_random_chars_and_random_chars(length, random_chars, random_chars_and_random_chars):
    """
    Returns a random string of length length and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars and random chars