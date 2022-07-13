
def string_to_hash(text):
    """
    Given a string 'text', return its sha256 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha256 hash equivalent hex string.
    If 'text' is an empty string, return None.
    """
    if text == '':
        return None
    return sha256(text.encode('utf-8')).hexdigest()


def hash_hex_to_string(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its string equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return hash_hex.decode('hex')


def hash_hex_to_int(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its integer equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return int(hash_hex, 16)


def hash_hex_to_bytes(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its bytes equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return bytes.fromhex(hash_hex)


def hash_hex_to_bytes(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its bytes equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return bytes.fromhex(hash_hex)


def hash_hex_to_bytes(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its bytes equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return bytes.fromhex(hash_hex)


def hash_hex_to_bytes(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its bytes equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return bytes.fromhex(hash_hex)


def hash_hex_to_bytes(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its bytes equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
    return bytes.fromhex(hash_hex)


def hash_hex_to_bytes(hash_hex):
    """
    Given a sha256 hash hex string 'hash_hex', return its bytes equivalent.
    If 'hash_hex' is an empty string, return None.
    """
    if hash_hex == '':
        return None
