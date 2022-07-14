def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "large" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n < 2000:
        return "large"
    else:
        return "small"


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


def get_random_float(length):
    """
        Returns a random float of length length.
    """
    return random.random() * float(length)


def get_random_date(length):
    """
        Returns a random date of length length.
    """
    return datetime.date.today() + datetime.timedelta(days=length)


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length)


def get_random_date_with_timezone(length):
    """
        Returns a random date of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, seconds=length)


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))


def get_random_datetime_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, seconds=length, microseconds=length)


def get_random_time_with_timezone(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))


def get_random_datetime_with_timezone_with