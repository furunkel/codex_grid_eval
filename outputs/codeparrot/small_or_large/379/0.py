def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "small" if n >= 2000 (and neither if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n < 2000:
        return "small"
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


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_timestamp(length):
    """
        Returns a random timestamp of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_array(length):
    """
        Returns a random array of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_boolean(length):
    """
        Returns a random boolean of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_enum(length):
    """
        Returns a random enum of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_array_of_strings(length):
    """
        Returns a random array of length length.
    """
    return ''.join(random.choice(string.