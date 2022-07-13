
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_hex_hash(hash):
    """
    Given a sha-384 hash string, return its hex hash equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return hash


def hash_to_bytes(hash):
    """
    Given a sha-384 hash string, return its bytes equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return hash.encode('utf-8')


def bytes_to_hex(hash):
    """
    Given a bytes string, return its hex equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return hash.encode('hex')


def hex_to_bytes(hash):
    """
    Given a hex string, return its bytes equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return bytes.fromhex(hash)


def bytes_to_int(hash):
    """
    Given a bytes string, return its integer equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_bytes(i):
    """
    Given an integer 'i', return its bytes equivalent string.
    If 'i' is an empty string, return None.
    """
    if i == '':
        return None
    return i.to_bytes((int_to_bytes(len(i))), 'big')


def int_to_hex(i):
    """
    Given an integer 'i', return its hex equivalent string.
    If 'i' is an empty string, return None.
    """
    if i == '':
        return None
    return i.to_bytes((int_to_bytes(len(i))), 'big').hex()


def hex_to_int(hash):
    """
    Given a hex string, return its integer equivalent string.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hex(i):
    """
    Given an integer 'i', return its hex equivalent string.
    If 'i' is an empty string, return None.
    """
    if i == '':
        return None
    return i.to_bytes((int_to_bytes(len(i))), '