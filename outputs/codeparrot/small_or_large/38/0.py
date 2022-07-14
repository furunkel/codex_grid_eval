def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "large" if n >= 15 (and neither if 2 <= n < 15).
    """
    if n < 2:
        return "small"
    elif n < 15:
        return "large"
    else:
        return "large"


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
    return ''.join(random.