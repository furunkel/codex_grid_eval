
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text:
        return sha1(text).hexdigest()
    else:
        return None


def string_to_hash_utf8(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text:
        return sha1(text.encode('utf-8')).hexdigest()
    else:
        return None


def string_to_hash_utf8_nopad(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_nopad('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text:
        return sha1(text.encode('utf-8')).hexdigest()
    else:
        return None


def string_to_hash_utf8_nopad_bytes(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_nopad_bytes('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text:
        return sha1(text.encode('utf-8')).hexdigest()
    else:
        return None


def string_to_hash_utf8_nopad_unicode(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_nopad_unicode('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text:
        return sha1(text.encode('utf-8')).hexdigest()
    else:
        return None


def string_to_hash_utf8_nopad_unicode_bytes(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_nopad_unicode_bytes('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text:
        return sha1(text.encode('utf-8')).hexdigest()
    else:
        return None


def string_to_hash_utf8_nopad_unicode_unicode(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_utf8_nopad_unicode_unicode('