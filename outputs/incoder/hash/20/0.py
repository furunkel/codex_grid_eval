
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_or_none(text):
    """
    Given a string 'text', return its sha1 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> string_to_hash_or_none('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_or_empty_string(text):
    """
    Given a string 'text', return its sha1 hash equivalent string or ''.
    If 'text' is an empty string, return ''.

    >>> string_to_hash_or_empty_string('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return ''
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_or_none_and_empty_string(text):
    """
    Given a string 'text', return its sha1 hash equivalent string or ''.
    If 'text' is an empty string, return None.

    >>> string_to_hash_or_none_and_empty_string('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_or_empty_string_and_none(text):
    """
    Given a string 'text', return its sha1 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> string_to_hash_or_empty_string_and_none('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    h = hashlib.sha1()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_or_none_and_empty_string_and_none(text):
    """
    Given a string 'text', return its sha1 hash equivalent string or None.
    If 'text' is an empty string, return None.

    >>> string_to_hash_or_none_and_empty_string_and_none('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '