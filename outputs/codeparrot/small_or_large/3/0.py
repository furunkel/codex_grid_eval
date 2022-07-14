def small_or_large(n):
    """
        Given an integer n, return "small" if n < -100 and "large" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return None
    elif n < 2000:
        return "large"
    else:
        return "small"


def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def get_random_int(length):
    """
        Returns a random integer of length length.
    """
    return random.randint(0, length)


def get_random_float(length):
    """
        Returns a random float of length length.
    """
    return random.uniform(0.0, 1.0)


def get_random_bool(length):
    """
        Returns a random bool of length length.
    """
    return random.choice([True, False])


def get_random_list(length):
    """
        Returns a random list of length length.
    """
    return [random.choice(string.ascii_lowercase) for _ in range(length)]


def get_random_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.choice(string.ascii_lowercase): random.choice(string.ascii_lowercase) for _ in range(length)}


def get_random_list_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.choice(string.ascii_lowercase): random.choice(string.ascii_lowercase) for _ in range(length)}


def get_random_dict_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.choice(string.ascii_lowercase): random.choice(string.ascii_lowercase) for _ in range(length)}


def get_random_list_list(length):
    """
        Returns a random list of length length.
    """
    return [random.choice(string.ascii_lowercase) for _ in range(length)]


def get_random_dict_list_dict(length):
    """
        Returns a random dict of length length.
    """