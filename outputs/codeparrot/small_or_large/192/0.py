def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "small" if n >= -1 (and None if -100 <= n < -1).
    """
    if n < -100:
        return "small"
    elif n < 0:
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

def get_random_timestamp(length):
    """
        Returns a random timestamp of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_decimal(length):
    """
        Returns a random decimal of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_boolean(length):
    """
        Returns a random boolean of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_enum(length):
    """
        Returns a random enum of length length.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_random_date_time(length):
    """
        Returns a random date and time of length length.
    """
    return ''.join