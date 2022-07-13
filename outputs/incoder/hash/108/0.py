
def string_to_hash(text):
    """
    Given a string 'text', return its blake2b hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if text == "":
        return None
    return blake2b(text.encode("utf-8"), digest_size=32)


def hash_to_string(hash):
    """
    Given a blake2b hash string, return its string equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash is None:
        return None
    return blake2b(hash.encode("utf-8"), digest_size=32).hex()


def hash_to_int(hash):
    """
    Given a blake2b hash string, return its integer equivalent.
    If 'hash' is an empty string, return None.
    """
    if hash is None:
        return None
    return int(hash, 16)


def int_to_hash(i):
    """
    Given an integer 'i', return its blake2b hash equivalent string.
    If 'i' is an empty string, return None.
    """
    if i is None:
        return None
    return blake2b(hex(i), digest_size=32).hex()


def int_to_string(i, length=8):
    """
    Given an integer 'i', return a string of length 'length' with its hex
    representation.
    If 'i' is an empty string, return None.
    """
    if i is None:
        return None
    return blake2b(hex(i), digest_size=length).hex()


def int_to_bytes(i):
    """
    Given an integer 'i', return a byte string with its hex representation.
    If 'i' is an empty string, return None.
    """
    if i is None:
        return None
    return blake2b(hex(i), digest_size=32).hex()


def bytes_to_int(b):
    """
    Given a byte string 'b', return its integer equivalent.
    If 'b' is an empty string, return None.
    """
    if b is None:
        return None
    return int(b, 16)


def bytes_to_string(s):
    """
    Given a byte string 's', return its string equivalent.
    If 's' is an empty string, return None.
    """
    if s is None:
        return None
    return s.hex()


def string_to_bytes(s):
    """
    Given a string 's', return its byte equivalent.
    If 's' is an empty string, return None.
    """
    if s is None:
        return None
    return s.encode("utf-8")


def bytes_to_int(b):
    """
    Given a byte string 'b', return its integer equivalent.
    If 'b' is an empty string, return None.
    """
    if b is None:
        return None
    return int(b, 16)


def int_to_bytes(i):
    """
    Given an integer 'i', return a byte string with its hex representation.
    If 'i' is an empty string, return None.
    """
    if i is None:
        return None
    return blake2b(hex(i), digest_size=32).hex()


def 