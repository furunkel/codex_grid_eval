
def string_to_hash(text):
    """
    Given a string 'text', return its sha-512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if text == '':
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex(text):
    """
    Given a string 'text', return its sha-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if text == '':
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str(text):
    """
    Given a string 'text', return its sha-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if text == '':
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str_str(text):
    """
    Given a string 'text', return its sha-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str_str('0') == '31bca02094eb78126a517b206a88c73cfa9ec6f704c7030d18212cace820f025f00bf0ea68dbf3f3a5436ca63b53bf7bf80ad8d5de7d8359d0b7fed9dbc3ab99'
    """
    if text == '':
        return None
    h = sha512()
    h.update(text.encode('utf-8'))
    return h.hexdigest()


def string_to_hash_hex_str_str_str(text):
    """
    Given a string 'text', return its sha-512 hash equivalent hex string.
    If 'text' is an empty string, return None.

    >>> string_to_hash_hex_str_str_str('0') == '31bca0