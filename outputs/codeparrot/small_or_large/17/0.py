def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "small"
    elif n < 2:
        return "large"
    else:
        return None


def get_random_string(length):
    """
        Returns a random string of the specified length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


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
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_date_time(length):
    """
        Returns a random date and time of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_time_date(length):
    """
        Returns a random date and time of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_datetime_time(length):
    """
        Returns a random datetime and time of the specified length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def get_random_time_datetime(length):
    """
        Returns