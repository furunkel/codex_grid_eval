
def string_to_hash(text):
    """
    Given a string 'text', return its sha3_512 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return hashlib.sha3_512(hash.encode('utf-8')).hexdigest()


def get_hash_value(hash):
    """
    Given a hash 'hash', return its integer value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def get_hash_range(hash):
    """
    Given a hash 'hash', return its range value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return int(hash, 16) % MAX_HASH_RANGE


def get_hash_range_start(hash):
    """
    Given a hash 'hash', return its range start value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return int(hash, 16) % MAX_HASH_RANGE


def get_hash_range_end(hash):
    """
    Given a hash 'hash', return its range end value.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return (int(hash, 16) + 1) % MAX_HASH_RANGE


def get_hash_range_start_from_value(value):
    """
    Given a hash value 'value', return its range start value.
    If 'value' is an empty string, return None.
    """
    if value == '':
        return None
    else:
        return value % MAX_HASH_RANGE


def