def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 2 and "large" if n >= 2000 (and None if 2 <= n < 2000).
    """
    if n < 2:
        return "mouse"
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
    return random.randint(1, length)


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


def get_random_date_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(length, timezone=timezone.get_default_timezone())


def get_random_datetime_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(length, timezone=timezone.get_default_timezone())


def get_random_datetime_with_timezone_offset(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(length, timezone=timezone.get_default_timezone(offset=1))


def get_random_datetime_with_timezone_offset_and_timezone(length):
    """
        Returns a random datetime of length length and timezone offset.
    """
    return datetime.datetime.now() + datetime.timedelta(length, timezone=timezone.get_default_timezone(offset=1, offset_type="timezone"))


def get_random_datetime_with_timezone_offset_and_timezone_offset_and_timezone_offset_and_timezone_offset_and_timezone_offset_and_timezone_offset