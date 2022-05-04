
def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8')).hexdigest()


def hash_to_string(hash):
    """
    Given a hash 'hash', return its string equivalent.
    If 'hash' is None, return an empty string.
    """
    if hash is None:
        return ''
    else:
        return hash


def hash_to_hex(hash):
    """
    Given a hash 'hash', return its hexadecimal equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    else:
        return hash.hex()


def hex_to_hash(hex):
    """
    Given a hexadecimal 'hex', return its hash equivalent.
    If 'hex' is None, return None.
    """
    if hex is None:
        return None
    else:
        return bytes.fromhex(hex)


def hash_to_base64(hash):
    """
    Given a hash 'hash', return its base64 equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    else:
        return base64.b64encode(hash).decode('utf-8')


def base64_to_hash(base64):
    """
    Given a base64 'base64', return its hash equivalent.
    If 'base64' is None, return None.
    """
    if base64 is None:
        return None
    else:
        return base64.b64decode(base64)


def hash_to_int(hash):
    """
    Given a hash 'hash', return its integer equivalent.
    If 'hash' is None, return None.
    """
    if hash is None:
        return None
    else:
        return int.from_bytes(hash, byteorder='big')


def int_to_hash(integer):
    """
    Given an integer 'integer', return its hash equivalent.
    If 'integer' is None, return None.
    """
    if integer