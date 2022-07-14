def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
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


def get_random_bool(min_value, max_value):
    """
        Returns a random boolean between min_value and max_value.
    """
    return random.choice([True, False])


def get_random_list(min_value, max_value):
    """
        Returns a random list between min_value and max_value.
    """
    return random.sample(xrange(min_value, max_value), random.randint(1, len(xrange(min_value, max_value))))


def get_random_dict(min_value, max_value):
    """
        Returns a random dict between min_value and max_value.
    """
    return {
        "min_value": min_value,
        "max_value": max_value,
    }


def get_random_list_dict(min_value, max_value):
    """
        Returns a random list dict between min_value and max_value.
    """
    return {
        "min_value": min_value,
        "max_value": max_value,
    }


def get_random_dict_list(min_value, max_value):
    """
        Returns a random list dict between min_value and max_value.
    """
    return {
        "min_value": min_value,
       