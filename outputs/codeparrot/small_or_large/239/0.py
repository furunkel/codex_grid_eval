def small_or_large(n):
    """
        Given an integer n, return "large" if n < 1000 and "small" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "small"
    elif n < 2000:
        return "large"
    else:
        return "small"


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


def get_random_bool(length):
    """
        Returns a random boolean of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_date_time(length):
    """
        Returns a random date and time of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_time_date(length):
    """
        Returns a random date and time of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_datetime_time(length):
    """
        Returns a random datetime and time of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_time_datetime(length):
    """
        Returns a random datetime and time of length length.
   