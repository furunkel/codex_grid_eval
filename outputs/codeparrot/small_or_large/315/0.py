def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < 10 and "large" if n >= 2000 (and None if 10 <= n < 2000).
    """
    if n < 10:
        return "mouse"
    elif n < 2000:
        return "large"
    else:
        return None


def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_int(length):
    """
        Returns a random integer of length length.
    """
    return random.randint(1, length)


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
    return [random.randint(1, length) for _ in range(length)]


def get_random_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z', '