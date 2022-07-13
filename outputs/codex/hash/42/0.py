
def string_to_hash(text):
    """
    Given a string 'text', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its SHA224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224((text + salt).encode('utf-8')).hexdigest()


def get_salt():
    """
    Return a random string of length 16.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))


def get_random_string(length):
    """
    Return a random string of length 'length'.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def get_random_string_with_prefix(prefix, length):
    """
    Return a random string of length 'length' with prefix 'prefix'.
    """
    return prefix + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(prefix)))


def get_random_string_with_suffix(suffix, length):
    """
    Return a random string of length 'length' with suffix 'suffix'.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(suffix))) + suffix


def get_random_string_with_prefix_and_suffix(prefix, suffix, length):
    """
    Return a random string of length 'length' with prefix 'prefix' and suffix 'suffix'.
    """
    return prefix + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(prefix) - len(suffix))) + suffix


def get_random