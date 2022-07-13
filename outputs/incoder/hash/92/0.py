
def string_to_hash(text):
    """
    Given a string 'text', return its sha512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    return sha512(text).hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    return sha512(text).hexdigest()


def string_to_hash_hex_unicode(text):
    """
    Given a string 'text', return its sha512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    return sha512(text.encode('utf-8')).digest()


def string_to_hash_hex_unicode_utf8(text):
    """
    Given a string 'text', return its sha512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode_utf8('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063f44cc4f219504312ea313e63c7cf60e01edd1f570a3edb'
    """
    if text == '':
        return None
    return sha512(text.encode('utf-8')).digest()


def string_to_hash_hex_unicode_utf8_unicode(text):
    """
    Given a string 'text', return its sha512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_unicode_utf8_unicode('Hallo welt') == '9c12b8eb6bc215a7d2202eaa0f255d5dbd6f6d820bbd7d936d7771691acb952904ef6a679ff4bf9063