
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
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

    >>> string_to_hash_hex('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
    """
    if text == '':
        return None
    h = hashlib.sha3_384()
    h.update(text.encode('utf-8'))
    return 