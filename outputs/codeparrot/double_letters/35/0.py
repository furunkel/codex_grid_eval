def double_letters(string):
    """
    Given a string, return the string, doubling every exclamation point character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.islower())


def get_random_string(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_length(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_letters(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_letters_and_length(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_string_with_letters_and_length_and_letters(length, letters, length_and_letters):
    """
    Returns a random string of the specified length and letters and length_and_letters.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length_and_letters))


def get_random_string_with_letters_and_length_and_letters_and_letters(length, letters, length_and_letters_and_letters):
    """
    Returns a random string of the specified length and letters and length_and_letters and length_and_letters_and_letters.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length_and_letters_and_letters))


def get_random_string_with_letters_and_length_and_letters_and_letters_and_letters(length, letters, length_and_