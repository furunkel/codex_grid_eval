
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    return blake2b(text.encode("utf-8"), digest_size=32).hexdigest()


def hash_to_string(hash):
    """
    Given a blake2b hash string, return its string equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    return blake2b(hash.encode("utf-8"), digest_size=32).hex()


def hash_to_int(hash):
    """
    Given a blake2b hash string, return its integer equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    return int(hash, 16)


def int_to_hash(i):
    """
    Given an integer 'i', return its blake2b hash equivalent string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    return blake2b(hex(i), digest_size=32).hex()


def int_to_hash_str(i):
    """
    Given an integer 'i', return its blake2b hash equivalent string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    return blake2b(hex(i), digest_size=32).hex()


def hash_to_int_str(hash):
    """
    Given a blake2b hash string, return its integer equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    return int(hash, 16)


def hash_to_int_int(hash):
    """
    Given a blake2b hash string, return its integer equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    return int(hash, 16)


def hash_to_int_list(hash_list):
    """
    Given a list of blake2b hash strings, return their integer equivalent.
    If 'hash' is None, return None.
    """
    if hash_list is None:
        return None
    return [int(hash, 16) for hash in hash_list]


def hash_to_int_set(hash_list):
    """
    Given a list of blake2b hash strings, return their integer equivalent.
    If 'hash' is None, return None.
    """
    if hash_list is None:
        return None
    return set(hash_list)


def hash_to_int_dict(hash_list):
    """
    Given a list of blake2b hash strings, return their integer equivalent.
    If 'hash' is None, return None.
    """
    if hash_list is None:
        return None
    return {int(hash, 16): True for hash in hash_list}


def hash_to_int_bool(hash):
    """
    Given a blake2b hash string, return its integer equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
