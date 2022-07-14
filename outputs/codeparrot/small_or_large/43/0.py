def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "large" if n >= 2000 (and neither if 10 <= n < 2000).
    """
    if n < 10:
        return "small"
    elif n < 2000:
        return "large"
    else:
        return "large"


def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_number(length):
    """
        Returns a random number of length length.
    """
    return random.randint(1, length)


def get_random_date(length):
    """
        Returns a random date of length length.
    """
    return datetime.date(random.randint(1, length), random.randint(1, length))


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime(random.randint(1, length), random.randint(1, length))


def get_random_date_range(length):
    """
        Returns a random date range of length length.
    """
    return range(length)


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(random.randint(1, length), random.randint(1, length))


def get_random_datetime_range(length):
    """
        Returns a random datetime range of length length.
    """
    return range(length)


def get_random_time_range(length):
    """
        Returns a random time range of length length.
    """
    return range(length)


def get_random_date_range_range(length):
    """
        Returns a random date range of length length.
    """
    return range(length)


def get_random_time_range_range(length):
    """
        Returns a random time range of length length.
    """
    return range(length)


def get_random_datetime_range_range(length):
    """
        Returns a random datetime range of length length.
    """
    return range(length)


def get_random_date_range_range(length):