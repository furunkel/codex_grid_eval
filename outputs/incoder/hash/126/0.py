
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
    Given a blake2s hash string 'hash', return its string equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return blake2s(hash.encode()).hexdigest()


def hash_to_int(hash):
    """
    Given a blake2s hash string 'hash', return its integer equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(num):
    """
    Given an integer 'num', return its blake2s hash equivalent string.
    If 'num' is an empty string, return None.
    """
    if num == '':
        return None
    return blake2s(num.to_bytes(32, byteorder='big')).digest()


def int_to_string(num):
    """
    Given an integer 'num', return its string equivalent.
    If 'num' is an empty string, return None.
    """
    if num == '':
        return None
    return blake2s(num.to_bytes(32, byteorder='big')).digest()


def int_to_bytes(num):
    """
    Given an integer 'num', return its bytes equivalent.
    If 'num' is an empty string, return None.
    """
    if num == '':
        return None
    return num.to_bytes(32, byteorder='big')


def bytes_to_int(bytes):
    """
    Given a bytes 'bytes', return its integer equivalent.
    If 'bytes' is an empty string, return None.
    """
    if bytes == b'':
        return None
    return int.from_bytes(bytes, byteorder='big')


def bytes_to_string(bytes):
    """
    Given a bytes 'bytes', return its string equivalent.
    If 'bytes' is an empty string, return None.
    """
    if bytes == b'':
        return None
    return bytes.hex()


def bytes_to_hex(bytes):
    """
    Given a bytes 'bytes', return its hex equivalent.
    If 'bytes' is an empty string, return None.
    """
    if bytes == b'':
        return None
    return bytes.hex()


def hex_to_bytes(hex):
    """
    Given a hex string 'hex', return its bytes equivalent.
    If 'hex' is an empty string, return None.
    """
    if hex == '':
        return None
    return bytes.fromhex(hex)


def hex_to_int(hex):
    """
    Given a hex string 'hex', return its integer equivalent.
    If 'hex' is an empty string, return None.
    """
    if hex == '':
        return None
    return int(hex, 