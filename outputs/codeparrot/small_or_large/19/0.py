def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "small"
    elif n < 2000:
        return "large"
    else:
        return None


def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_int(length):
    """
        Returns a random integer of length length.
    """
    return random.randint(0, length)


def get_random_float(length):
    """
        Returns a random float of length length.
    """
    return random.uniform(0.0, 1.0)


def get_random_bool(length):
    """
        Returns a random bool of length length.
    """
    return random.choice([True, False])


def get_random_date(length):
    """
        Returns a random date of length length.
    """
    return datetime.date.today() + datetime.timedelta(days=length)


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(0, 0, 0)


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length)


def get_random_date_time(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length)


def get_random_time_date(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.date.today() + datetime.timedelta(days=length)


def get_random_datetime_time(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.time(0, 0, 0)


def get_random_date_time_time(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.time(0, 0, 0)


