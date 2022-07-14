def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return "".join([char for char in string if char not in string.punctuation])


def get_random_string(length):
    """
    Returns a random string of length length.
    """
    return "".join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_length(length):
    """
    Returns a random string of length length.
    """
    return "".join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_length_and_random_chars(length, random_chars):
    """
    Returns a random string of length length and random characters.
    """
    return "".join([random.choice(string.letters) for _ in range(length)]) + random_chars


def get_random_string_with_length_and_random_chars_and_random_chars(length, random_chars, random_chars_and_random_chars):
    """
    Returns a random string of length length and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters and random characters