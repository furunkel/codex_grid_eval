def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "house" if n >= 2000 (and None if 2 <= n < 2000).
    """
    if n < 2:
        return "small"
    elif n < 2000:
        return "large"
    else:
        return None


def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_number(length):
    """
        Returns a random number of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_date(length):
    """
        Returns a random date of length length.
    """
    return datetime.date(random.randint(1, 12), random.randint(1, 28), random.randint(1, 30))


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime(random.randint(1, 12), random.randint(1, 28), random.randint(1, 30))


def get_random_date_range(length):
    """
        Returns a random date range of length length.
    """
    return (datetime.date(random.randint(1, 12), random.randint(1, 28), random.randint(1, 30)) for _ in range(length))


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(random.randint(1, 12), random.randint(1, 28), random.randint(1, 30))


def get_random_datetime_range(length):
    """
        Returns a random datetime range of length length.
    """
    return (datetime.datetime(random.randint(1, 12), random.randint(1, 28), random.randint(1, 30)) for _ in range(length))


def get_random_time_range(length):
    """
        Returns a random time range of length length.
    """
    return (datetime.time(random.randint(1, 12), random.randint(1, 28), random.randint