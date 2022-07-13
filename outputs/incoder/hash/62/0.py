
def string_to_hash(text):
    """
    Given a string 'text', return its SHA256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def string_to_hash_base64(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).digest()


def string_to_hash_base64_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_hex('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).digest()


def string_to_hash_base64_utf8(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 utf8 string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """
    if text == '':
        return None
    return hashlib.sha256(text.encode('utf-8')).digest()


def string_to_hash_base64_utf8_hex(text):
    """
    Given a string 'text', return its SHA256 hash equivalent base64 utf8 hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_base64_utf8_hex('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b