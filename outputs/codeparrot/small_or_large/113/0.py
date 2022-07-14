def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < -100:
        return "small"
    elif n < 2:
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
    return datetime.date.today() + datetime.timedelta(days=length)


def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length)


def get_random_date_range(length):
    """
        Returns a random date range of length length.
    """
    return (datetime.date.today() + datetime.timedelta(days=length)).strftime("%Y-%m-%d")


def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))


def get_random_datetime_range(length):
    """
        Returns a random datetime range of length length.
    """
    return (datetime.datetime.now() + datetime.timedelta(days=length)).strftime("%Y-%m-%d %H:%M:%S")


def get_random_time_range(length):
    """
        Returns a random time range of length length.
    """
    return (datetime.time(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))
            ).strftime("%H:%M:%S")


def get_random_date_range(length):
   