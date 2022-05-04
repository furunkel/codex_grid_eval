
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_with_salt(text, salt):
    """
    Given a string 'text' and a string 'salt', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224((text + salt).encode('utf-8')).hexdigest()


def get_random_string(length):
    """
    Given an integer 'length', return a random string of length 'length'.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def get_random_string_with_prefix(prefix, length):
    """
    Given a string 'prefix' and an integer 'length', return a random string of length 'length'
    with 'prefix' as its prefix.
    """
    return prefix + get_random_string(length - len(prefix))


def get_random_string_with_suffix(suffix, length):
    """
    Given a string 'suffix' and an integer 'length', return a random string of length 'length'
    with 'suffix' as its suffix.
    """
    return get_random_string(length - len(suffix)) + suffix


def get_random_string_with_prefix_and_suffix(prefix, suffix, length):
    """
    Given a string 'prefix', a string 'suffix', and an integer 'length', return a random string
    of length 'length' with 'prefix' as its prefix and 'suffix' as its suffix.
    """
    return prefix + get_random_string(length - len(prefix) - len(suffix)) + suffix


def get_random_string_with_prefix_and_suffix_and_length(prefix, suffix, length):
    """
    Given a string 'prefix', a string 'suffix', and an integer 'length', return a random