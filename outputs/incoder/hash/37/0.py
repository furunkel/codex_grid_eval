
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_utf8(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return hashlib.sha224(text.encode('utf-8')).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    return hashlib.sha224(text).hexdigest()


def string_to_hash_utf8