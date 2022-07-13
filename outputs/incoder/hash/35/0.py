
def string_to_hash(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text:
        return sha1(text).hexdigest()
    return None


def string_to_hash_or_none(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> string_to_hash_or_none('md5') is None
    """
    if text:
        return sha1(text).hexdigest()
    return None


def string_to_hash_or_empty(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or empty string.
    If 'text' is an empty string, return empty string.

    >>> string_to_hash_or_empty('md5') == 'c1ea94f7e524679d0cf34ab7b0b28abe41ba732b'
    """
    if text:
        return sha1(text).hexdigest()
    return ''


def string_to_hash_or_empty_or_none(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or empty string or
    None.
    If 'text' is an empty string, return empty string.

    >>> string_to_hash_or_empty_or_none('md5') is None
    """
    if text:
        return sha1(text).hexdigest()
    return ''


def string_to_hash_or_empty_or_none_or_blank(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or empty string or
    None.
    If 'text' is an empty string, return empty string.

    >>> string_to_hash_or_empty_or_none_or_blank('md5') is None
    """
    if text:
        return sha1(text).hexdigest()
    return ''


def string_to_hash_or_empty_or_none_or_blank_or_none(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or empty string or
    None.
    If 'text' is an empty string, return empty string.

    >>> string_to_hash_or_empty_or_none_or_blank_or_none('md5') is None
    """
    if text:
        return sha1(text).hexdigest()
    return None


def string_to_hash_or_empty_or_none_or_blank_or_none_or_blank(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or empty string or
    None.
    If 'text' is an empty string, return empty string.

    >>> string_to_hash_or_empty_or_none_or_blank_or_none_or_blank('md5') is None
    """
    if text:
        return sha1(text).hexdigest()
    return None


def string_to_hash_or_empty_or_none_or_blank_or_none_or_blank_or_none(text):
    """
    Given a string 'text', return its sha-1 hash equivalent string or empty string or
    None.