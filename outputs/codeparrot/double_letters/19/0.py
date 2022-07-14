def double_letters(string):
    """
    Given a string, return the string, doubling every upper-case letter character, and tripling every lower-case letter.
    All other characters should be output a single time each.
    """
    return ''.join(c for c in string if c.isupper())


def get_random_string(length):
    """
    Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_number(length):
    """
    Returns a random number of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_date(length):
    """
    Returns a random date of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_datetime(length):
    """
    Returns a random datetime of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_time(length):
    """
    Returns a random time of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_bool(length):
    """
    Returns a random boolean of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_float(length):
    """
    Returns a random float of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_int(length):
    """
    Returns a random integer of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_list(length):
    """
    Returns a random list of the specified length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_dict(length):
    """
    Returns a random dict of the specified length