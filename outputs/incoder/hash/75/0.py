
def string_to_hash(text):
    """
    Given a string 'text', return its sha384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    h = sha384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def hash_to_string(hash):
    """
    Given a sha384 hash string, return its string equivalent string.
    If 'hash' is an empty string, return None.

    >>> hash_to_string('5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b') == '0'
    """
    if hash == '':
        return None
    return hash.encode('utf-8')


def hash_to_int(hash):
    """
    Given a sha384 hash string, return its integer equivalent string.
    If 'hash' is an empty string, return None.

    >>> hash_to_int('5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b') == 0
    """
    if hash == '':
        return None
    return int(hash, 16)


def int_to_hash(num):
    """
    Given an integer 'num', return its sha384 hash equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_hash(0) == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if num == '':
        return None
    h = sha384()
    h.update(str(num).encode('utf-8'))
    return h.hexdigest()


def int_to_string(num):
    """
    Given an integer 'num', return its string equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_string(0) == '0'
    """
    if num == '':
        return None
    return str(num).encode('utf-8')


def int_to_bytes(num):
    """
    Given an integer 'num', return its bytes equivalent string.
    If 'num' is an empty string, return None.

    >>> int_to_bytes(0) == b'\x00'
    """
    if num == '':
        return None
    return bytes(num)


def bytes_to_int(bytes):
    """
    Given a bytes 'bytes', return its integer equivalent string.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_int(b'\x00') == 0
    """
    if bytes == b'':
        return None
    return int(bytes.hex(), 16)


def bytes_to_string(bytes):
    """
    Given a bytes 'byte