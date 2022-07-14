def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "small"
    elif n < 2000:
        return "large"
    else:
        return None


def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_number(length):
    """
        Returns a random number of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_date(length):
    """
        Returns a random date of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_bool(length):
    """
        Returns a random bool of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_date_time(length):
    """
        Returns a random date time of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_time_zone(length):
    """
        Returns a random time zone of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_datetime_tz(length):
    """
        Returns a random datetime zone of length length.
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def get_random_time_zone_time(length):
    """
        Returns a random time zone of length length.
    """
    return "".