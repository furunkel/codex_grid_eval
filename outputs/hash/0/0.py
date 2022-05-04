
def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.md5((text + salt).encode()).hexdigest()


def get_random_string(length):
    """
    Return a random string of length 'length'.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def get_random_string_with_prefix(prefix, length):
    """
    Return a random string of length 'length' with prefix 'prefix'.
    """
    return prefix + get_random_string(length)


def get_random_string_with_suffix(suffix, length):
    """
    Return a random string of length 'length' with suffix 'suffix'.
    """
    return get_random_string(length) + suffix


def get_random_string_with_prefix_and_suffix(prefix, suffix, length):
    """
    Return a random string of length 'length' with prefix 'prefix' and suffix 'suffix'.
    """
    return prefix + get_random_string(length) + suffix


def get_random_string_with_prefix_and_suffix_and_length(prefix, suffix, length):
    """
    Return a random string of length 'length' with prefix 'prefix' and suffix 'suffix'.
    """
    return prefix + get_random_string(length) + suffix


def get_random_string_with_prefix_and_length(prefix, length):
    """
    Return a random string of length 'length' with prefix 'prefix'.
    """
    return prefix + get_random_string(length)


def get_random_string_with_suffix_and_length(suffix,