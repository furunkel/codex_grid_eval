def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every upper-case letter.
    All other characters should be output a single time each.
    """
    return ''.join([char for char in string if char.isupper()])


def get_random_string(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_length(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_letters(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_length_and_letters(length, letters):
    """
    Returns a random string of the specified length and letters.
    """
    return ''.join([random.choice(string.letters) for _ in range(length), ''.join(letters)])


def get_random_string_with_letters_and_length(length, letters, length_and_letters):
    """
    Returns a random string of the specified length and letters and length_and_letters.
    """
    return ''.join([random.choice(string.letters) for _ in range(length), ''.join(letters), ''.join(length_and_letters)])


def get_random_string_with_letters_and_length_and_letters(length, letters, length_and_letters, length_and_letters_and_length):
    """
    Returns a random string of the specified length and letters and length_and_letters and length_and_letters_and_length.
    """
    return ''.join([random.choice(string.letters) for _ in range(length), ''.join(letters), ''.join(length_and_letters), ''.join(length_and_letters_and_length)])


def get_random_string_with_letters_and_length_and_letters_and_length(length, letters, length_and_letters, length_and_letters