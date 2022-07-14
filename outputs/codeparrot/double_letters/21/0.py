def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isupper())


def get_random_string(length):
    """
    Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_number(length):
    """
    Returns a random number of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_date(length):
    """
    Returns a random date of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_datetime(length):
    """
    Returns a random datetime of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_bool(length):
    """
    Returns a random boolean of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_float(length):
    """
    Returns a random float of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_int(length):
    """
    Returns a random integer of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_list(length):
    """
    Returns a random list of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_dict(length):
    """
    Returns a random dict of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_list_dict(length):
    """
    Returns a random dict of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _