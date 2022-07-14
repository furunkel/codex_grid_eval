def small_or_large(n):
    """
        Given an integer n, return "large" if n < 10 and "small" if n >= 15 (and None if 10 <= n < 15).
    """
    if n < 10:
        return "small"
    elif n < 15:
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
    return ''.join(random.choice(date.today().strftime('%Y-%m-%d') for _ in range(length))

def get_random_datetime(length):
    """
        Returns a random datetime of the specified length.
    """
    return ''.join(random.choice(datetime.now().strftime('%Y-%m-%d') for _ in range(length))

def get_random_time(length):
    """
        Returns a random time of the specified length.
    """
    return ''.join(random.choice(time.localtime()) for _ in range(length))

def get_random_timestamp(length):
    """
        Returns a random timestamp of the specified length.
    """
    return ''.join(random.choice(datetime.now().strftime('%Y-%m-%d %H:%M:%S') for _ in range(length))

def get_random_decimal(length):
    """
        Returns a random decimal of the specified length.
    """
    return ''.join(random.choice(decimal.Decimal(str(random.randint(0, 9)) for _ in range(length)))

def get_random_boolean(length):
    """
        Returns a random boolean of the specified length.
    """
    return ''.join(random.choice(boolean.TRUE_STRINGS) for _ in range(length))

def get_random_date_time(length):
    """
        Returns a random date and time of the specified length.
    """
    return ''.join(random