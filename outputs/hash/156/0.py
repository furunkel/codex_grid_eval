
def string_to_hash(text):
    """
    Given a string 'text', return its sha3-512 hash equivalent string.
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


def get_hash_values(hashes):
    """
    Given a list of hashes 'hashes', return a list of their integer values.
    If 'hashes' is an empty list, return None.
    """
    if hashes == []:
        return None
    else:
        return [get_hash_value(hash) for hash in hashes]


def get_hash_range(hash):
    """
    Given a hash 'hash', return its range of values.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    else:
        return (get_hash_value(hash), get_hash_value(hash) + 1)


def get_hash_ranges(hashes):
    """
    Given a list of hashes 'hashes', return a list of their ranges of values.
    If 'hashes' is an empty list, return None.
    """
    if hashes == []:
        return None
    else:
        return [get_hash_range(hash) for hash in hashes]


def get_hash_range_from_string(text):
    """
    Given a string 'text', return its range of values.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return