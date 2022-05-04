
def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a SHA3_512 hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return hashlib.sha3_512(hash.encode('utf-8')).hexdigest()


def get_hash_value(hash):
    """
    Given a SHA3_512 hash 'hash', return its integer value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def get_hash_range(hash):
    """
    Given a SHA3_512 hash 'hash', return its range value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return int(hash, 16) % MAX_HASH_RANGE


def get_hash_range_from_string(text):
    """
    Given a string 'text', return its SHA3_512 hash range value.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return get_hash_range(string_to_hash(text))


def get_hash_range_from_value(value):
    """
    Given an integer 'value', return its SHA3_512 hash range value.
    If 'value' is None, return None.
    """
    if value is None:
        return None
    else:
        return get_hash_range(value_to_hash(value))


def get_hash_range_from_hash(hash):
    """
    Given a SHA3_512 hash 'hash', return its range value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
