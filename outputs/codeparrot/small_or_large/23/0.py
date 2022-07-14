def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "large" if n >= 2000 (and None if 2 <= n < 2000).
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
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

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

def get_random_date_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length)

def get_random_datetime_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length, minutes=length)

def get_random_datetime_with_timezone_and_date(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length, minutes=length, seconds=length)

def get_random_datetime_with_timezone_and_date_and_time(length):
    """
        Returns a random datetime of length length.
    """
    return datetime.datetime.now() + datetime.timedelta(days=length, hours=length, minutes=length, seconds=length)

def get_random_datetime_with_timezone_and_date_and_time_and_timezone(length):
    """
        Returns a random datetime of