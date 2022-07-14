def small_or_large(n):
    """
        Given an integer n, return "large" if n < 10 and "small" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
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

def get_random_number(length):
    """
        Returns a random number of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_date(length):
    """
        Returns a random date of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_datetime(length):
    """
        Returns a random datetime of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_time(length):
    """
        Returns a random time of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_datetime_with_timezone(length):
    """
        Returns a random datetime of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_time_with_timezone(length):
    """
        Returns a random time of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_datetime_with_timezone_and_offset(length):
    """
        Returns a random datetime of length length and offset.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_datetime_with_timezone_and_offset_and_timezone(length, offset, timezone):
    """
        Returns a random datetime of length length and offset and timezone.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def