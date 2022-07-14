def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 1000 and "small" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "mouse"
    elif n < 2000:
        return "small"
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
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length)


def get_random_datetime_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length, minutes=length)


def get_random_datetime_with_timezone_and_offset(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length, minutes=length, seconds=length)


def get_random_datetime_with_timezone_and_offset_and_timezone(length):
    """
        Returns a random datetime of length length and timezone.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length, minutes=length, seconds=length, timezone=length)


def get_random_datetime_with_timezone_and_offset_and_timezone_and_offset(length):
    """
        Returns a random datetime of length length and timezone and offset