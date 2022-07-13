
def string_to_hash(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '05b7f4cbafdb32436fe8928f41ed8f64'
    """
    if not text:
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()


def string_to_bytes(text, encoding='utf-8'):
    """
    Given a string 'text', return its bytes equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bytes('Hallo welt') == 'Hallo welt'
    """
    if not text:
        return None
    return text.encode(encoding)


def bytes_to_string(bytes, encoding='utf-8'):
    """
    Given a bytes 'bytes', return its string equivalent string.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_string('Hallo welt') == 'Hallo welt'
    """
    if not bytes:
        return None
    return bytes.decode(encoding)


def bytes_to_int(bytes, encoding='utf-8'):
    """
    Given a bytes 'bytes', return its integer equivalent string.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_int('Hallo welt') == 13
    """
    if not bytes:
        return None
    return int(bytes.decode(encoding))


def int_to_bytes(number, encoding='utf-8'):
    """
    Given an integer 'number', return its bytes equivalent string.
    If 'number' is an empty string, return None.

    >>> int_to_bytes(13) == 'Hallo welt'
    """
    if not number:
        return None
    return str(number).encode(encoding)


def int_to_string(number, encoding='utf-8'):
    """
    Given an integer 'number', return its string equivalent string.
    If 'number' is an empty string, return None.

    >>> int_to_string(13) == 'Hallo welt'
    """
    if not number:
        return None
    return str(number)


def string_to_bytes(text, encoding='utf-8'):
    """
    Given a string 'text', return its bytes equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bytes('Hallo welt') == 'Hallo welt'
    """
    if not text:
        return None
    return text.encode(encoding)


def bytes_to_string(bytes, encoding='utf-8'):
    """
    Given a bytes 'bytes', return its string equivalent string.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_string('Hallo welt') == 'Hallo welt'
    """
    if not bytes:
        return None
    return bytes.decode(encoding)


def bytes_to_int(bytes, encoding='utf-8'):
    """
    Given a bytes 'bytes', return its integer equivalent string.
    If 'bytes' is an empty string, return None.

    >>> bytes_to_int('Hallo welt') == 13
    """
    if not bytes:
        return None
    return int(bytes.decode(encoding))


def int_to_bytes(number, encoding='utf-8'):
    """
    Given an integer 'number', return its bytes equivalent string.
    If 'number' is an empty string, return 