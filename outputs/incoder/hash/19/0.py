
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text).hexdigest()


def string_to_hash_utf8(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text.encode('utf-8')).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text.encode('ascii', 'ignore')).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text.encode('ascii', 'ignore')).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text.encode('ascii', 'ignore')).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """
    if text == '':
        return None
    return sha1(text.encode('ascii', 'ignore')).hexdigest()


def string_to_hash_utf8_no_unicode(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_no_unicode('Hello world') == '7b502c3a1f48c860