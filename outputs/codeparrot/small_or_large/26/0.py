def small_or_large(n):
    """
        Given an integer n, return "small" if n < 10 and "large" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "small"
    elif n < 15:
        return "large"
    else:
        return None


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
    return datetime.date.today() + datetime.timedelta(length)


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(length)


def get_random_date_range(length):
    """
        Returns a random date range of length length.
    """
    return (datetime.date.today() + datetime.timedelta(length)).strftime('%Y-%m-%d')


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(0, 0, 0) + datetime.timedelta(length)


def get_random_datetime_range(length):
    """
        Returns a random datetime range of length length.
    """
    return (datetime.datetime.now() + datetime.timedelta(length)).strftime('%Y-%m-%d %H:%M:%S')


def get_random_time_range(length):
    """
        Returns a random time range of length length.
    """
    return (datetime.time(0, 0, 0) + datetime.timedelta(length)).strftime('%H:%M:%S')


def get_random_date_range(length):
    """
        Returns a random date range of length length.
    """
    return (datetime.date.today() + datetime.timedelta(length)).strftime('%Y-%m-%d')


def get_random_time_range(length):
   