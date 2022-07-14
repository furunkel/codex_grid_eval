def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "house" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n < 2000:
        return "house"
    else:
        return None


def get_random_number(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_float(min_value, max_value):
    """
        Returns a random float between min_value and max_value.
    """
    return random.uniform(min_value, max_value)


def get_random_int(min_value, max_value):
    """
        Returns a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_float_or_none(min_value, max_value):
    """
        Returns a random float between min_value and max_value.
    """
    return get_random_float(min_value, max_value) if max_value is not None else None


def get_random_int_or_none(min_value, max_value):
    """
        Returns a random integer between min_value and max_value.
    """
    return get_random_int(min_value, max_value) if max_value is not None else None


def get_random_float_or_none_or_empty(min_value, max_value):
    """
        Returns a random float between min_value and max_value.
    """
    return get_random_float(min_value, max_value) if max_value is not None else None


def get_random_int_or_none_or_empty(min_value, max_value):
    """
        Returns a random integer between min_value and max_value.
    """
    return get_random_int(min_value, max_value) if max_value is not None else None


def get_random_float_or_none_or_empty(min_value, max_value):
    """
       