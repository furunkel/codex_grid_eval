def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "large" if n >= 2000 (and neither if 2 <= n < 2000).
    """
    if n < 2:
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
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, seconds=timezone.get_current_timezone())


def get_random_datetime_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, seconds=timezone.get_current_timezone())


def get_random_datetime_with_timezone_with_offset(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, seconds=timezone.get_current_timezone(offset=length))


def get_random_datetime_with_timezone_with_offset_and_timezone(length):
    """
        Returns a random datetime of length length and timezone.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, seconds=timezone.get_current_timezone(offset=length, offset_timezone=True))


def get_random_datetime_with_timezone_with_offset_and_timezone_with_timezone_offset(