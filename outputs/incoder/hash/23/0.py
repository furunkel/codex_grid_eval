
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def string_to_hash_int(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    return int(hashlib.sha1(text.encode('utf-8')).hexdigest(), 16)


def string_to_hash_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5', 8) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    return int(hashlib.sha1(text.encode('utf-8')).hexdigest(), 16)[:length]


def string_to_hash_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5', 8) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    return int(hashlib.sha1(text.encode('utf-8')).hexdigest(), 16)[:length]


def string_to_hash_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5', 8) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    return int(hashlib.sha1(text.encode('utf-8')).hexdigest(), 16)[:length]


def string_to_hash_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5', 8) == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text == '':
        return None
    return int(hashlib.sha1(text.encode('utf-8')).hexdigest(), 16)[:length]


def string_to_hash_int(text, length=8):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_int('md5', 8) == 'c1ea94f