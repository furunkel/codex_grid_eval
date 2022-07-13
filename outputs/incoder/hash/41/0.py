
def string_to_hash(text):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_with_prefix(text, prefix):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefix('md5', 'prefix') == 'prefix9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    return prefix + h.hexdigest()


def string_to_hash_with_prefixes(text, prefixes):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefixes('md5', 'prefix') == 'prefix9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    for prefix in prefixes:
        prefix = prefix + ':'
    return prefix + h.hexdigest()


def string_to_hash_with_prefixes_and_suffix(text, prefixes, suffix):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefixes_and_suffix('md5', 'prefix', 'suffix') == 'prefix9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3suffix'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    for prefix in prefixes:
        prefix = prefix + ':'
    return prefix + h.hexdigest() + suffix


def string_to_hash_with_prefixes_and_suffix_and_prefix(text, prefixes, suffix, prefix):
    """
    Given a string 'text', return its sha224 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_with_prefixes_and_suffix_and_prefix('md5', 'prefix', 'suffix', 'prefix') == 'prefix9f1a17462e4842ba55e6378178242a9a5e8840f83e2bf6c0e2faacc3suffix'
    """
    if not text:
        return None
    h = hashlib.sha224()
    h.update(text.encode('utf-8'))
    for prefix in prefixes:
        prefix = prefix + ':'
    return prefix + 