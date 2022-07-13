
def string_to_hash(text):
    """
    Given a string 'text', return its sha-384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    return hashlib.sha3_384(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-384 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    return hashlib.sha3_384(text.encode('utf-8')).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its sha-384 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    return hashlib.sha3_384(text.encode('utf-8')).digest()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its sha-384 hash equivalent base64 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    return hashlib.sha3_384(text.encode('utf-8')).digest()


def string_to_hash_base64_str(text):
    """
    Given a string 'text', return its sha-384 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_str('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    return hashlib.sha3_384(text.encode('utf-8')).digest()


def string_to_hash_base64_str_hex(text):
    """
    Given a string 'text', 