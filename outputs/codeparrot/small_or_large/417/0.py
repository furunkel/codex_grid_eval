def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 2 (and neither if -100 <= n < 2).
    """
    if n < -100:
        return "mouse"
    elif n < 2:
        return "house"
    else:
        return "large"


def get_random_number(min_value, max_value):
    """
        Returns a random number between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_float(min_value, max_value):
    """
        Returns a random float between min_value and max_value.
    """
    return random.random() * (max_value - min_value) + min_value


def get_random_int(min_value, max_value):
    """
        Returns a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_random_bool(min_value, max_value):
    """
        Returns a random boolean between min_value and max_value.
    """
    return random.random() > 0.5


def get_random_float_list(min_value, max_value):
    """
        Returns a random list of random floats between min_value and max_value.
    """
    return random.sample(get_random_float(min_value, max_value), 1)[0]


def get_random_int_list(min_value, max_value):
    """
        Returns a random list of random ints between min_value and max_value.
    """
    return random.sample(get_random_int(min_value, max_value), 1)[0]


def get_random_float_list_list(min_value, max_value):
    """
        Returns a random list of random floats between min_value and max_value.
    """
    return random.sample(get_random_float_list(min_value, max_value), 1)[0]


def get_random_int_list_list(min_value, max_value):
    """
        Returns a random list of random ints between min_value and max_value.