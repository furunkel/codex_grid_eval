def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 2000 (and None if -100 <= n < 2000).
    """
    if n < -100:
        return "mouse"
    elif n < 2000:
        return "small"
    else:
        return None

def get_random_string(length):
    """
        Returns a random string of length length.
    """
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

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
    return [random.randint(0, length) for _ in range(length)]

def get_random_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.randint(0, length): random.randint(0, 100) for _ in range(length)}

def get_random_list_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.randint(0, length): random.randint(0, 100) for _ in range(length)}

def get_random_dict_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.randint(0, length): random.randint(0, 100) for _ in range(length)}

def get_random_list_dict_dict(length):
    """
        Returns a random dict of length length.
    """
    return {random.randint(0, length): random.randint(0, 100) for _ in range(length)}

def get_random_dict_list(length):
    """
        Returns a random list of length length.
    """
    return [random.randint(0