
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return blake2s(text.encode()).hexdigest()


def hash_to_string(hash):
    """
    Given a blake2s hash string, return its string equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    return blake2s(hash.encode()).hexdigest()


def hash_to_int(hash):
    """
    Given a blake2s hash string, return its integer equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    return int(hash, 16)


def int_to_hash(i):
    """
    Given an integer 'i', return its blake2s hash equivalent string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    return blake2s(struct.pack('>Q', i).encode()).hexdigest()


def int_to_string(i, length=None):
    """
    Given an integer 'i', return its string equivalent.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    if length is None:
        return blake2s(struct.pack('>Q', i).encode()).hexdigest()
    return blake2s(struct.pack('>Q', i).encode()).hexdigest()[:length]


def int_to_hash_hex(i):
    """
    Given an integer 'i', return its blake2s hash equivalent hex string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    return blake2s(struct.pack('>Q', i).encode()).hexdigest()


def int_to_hash_hex_len(i, length=None):
    """
    Given an integer 'i', return its blake2s hash equivalent hex string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    if length is None:
        return blake2s(struct.pack('>Q', i).encode()).hexdigest()
    return blake2s(struct.pack('>Q', i).encode()).hexdigest()[:length]


def int_to_hash_hex_len_hex(i):
    """
    Given an integer 'i', return its blake2s hash equivalent hex string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    return blake2s(struct.pack('>Q', i).encode()).hexdigest()


def int_to_hash_hex_len_hex_len(i, length=None):
    """
    Given an integer 'i', return its blake2s hash equivalent hex string.
    If 'i' is None, return None.
    """
    if i is None:
        return None
    if length is None:
        return blake2s(struct.pack('>Q', 